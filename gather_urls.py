# from bs4 import BeautifulSoup
# from bs4.element import Comment
# import requests
#
# url_base = 'https://www.google.com/search?q='
#
# def get_google_search(input):
#     rest = ''
#     for string in input.split(' '):
#         rest += string
#         rest += '+'
#     return url_base + rest[:-1]
#
# # def parse_html_for_hrefs(html):
#
# def get_urls(input):
#     url = get_google_search(input)
#     html = requests.get(url).text
#     soup = BeautifulSoup(html, 'html.parser')
#     print(soup.find_all('cite'))
#
# get_urls('orange peels')

from googlesearch import search

def get_urls(input, num_results=10):
    return list(search(input, tld="co.in", num=num_results, stop=1, pause=2))
