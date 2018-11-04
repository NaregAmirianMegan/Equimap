from bs4 import BeautifulSoup
from bs4.element import Comment
import requests
import execnet

# from gather_urls import get_urls

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
    soup = BeautifulSoup(body, 'html.parser')
    texts = soup.findAll(text=True)
    visible_texts = filter(tag_visible, texts)
    return u" ".join(t.strip() for t in visible_texts)

def compile_corpus(input, num_results=10):
    urls = call_python_version("2.7", "gather_urls", "get_urls",
                                 [input, num_results])
    text_list = []
    for url in urls:
        html = requests.get(url).text
        text_list.append(text_from_html(html))
    return text_list

print(compile_corpus('tesla', 2))
