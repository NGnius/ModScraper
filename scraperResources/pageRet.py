import urllib.request
page=""
def pageRet(url):
    global page
    page = urllib.request.urlopen(url).read()
    return page
