#!/usr/bin/env python3

import urllib.parse

def to_readit_url(url):
    return("https://www.google.com/readit?url=" + urllib.parse.quote(url, safe=""))

if __name__ == '__main__':
    import sys
    print(toGoogleURL(sys.argv[1]))
