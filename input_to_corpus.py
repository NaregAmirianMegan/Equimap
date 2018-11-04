from bs4 import BeautifulSoup
from bs4.element import Comment
import requests, execnet

url_base = 'https://www.google.com/search?q='

def get_google_url(input):
    rest = ''
    for string in input.split(' '):
        rest += string
        rest += '+'
    return url_base + rest[:-1]

def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]', 'a', 'ul', 'ol', 'li']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = BeautifulSoup(body, 'lxml')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

# def get_lat_long(input):
#     google_url = get_google_url(input)
#     soup = BeautifulSoup(requests.get(google_url).text, 'lxml')
#     hq = soup.find(text='Headquarters').a.next_sibling
#     return hq

def compile_corpus(input, num_results=1):
    # lat, long = get_lat_long(input)
    urls = call_python_version("2.7", "gather_urls", "get_urls",
                                 [input, num_results])
    text_list = []
    for url in urls:
        html = requests.get(url).text
        text_list.append(text_from_html(html))
    return text_list
#( , lat, long)
