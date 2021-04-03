import urllib.parse

def toGoogleURL(url):
    return("https://www.google.com/readit?url=" + urllib.parse.quote(url, safe=""))

if __name__ == '__main__':
    import sys
    print(toGoogleURL(sys.argv[1]))
