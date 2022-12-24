#!/usr/bin/env python3

import sys
import requests
from bs4 import BeautifulSoup

def get_links_of_url(url):
    '''lists all urls from web page'''
    page = requests.get(url)

    if page.status_code == 200:
        dom = BeautifulSoup(page.text, 'html.parser')
    else:
        raise ValueError("HTTP request failed")

    return [link.get('href') for link in dom.find_all('a')]

if __name__ == '__main__' and len(sys.argv) == 2:
    print(get_links_of_url(sys.argv[1]))
