from googlesearch import search

def get_urls(input, num_results=10):
    return list(search(input, tld="co.in", num=num_results, stop=1, pause=2))
