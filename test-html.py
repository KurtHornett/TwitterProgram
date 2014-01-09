from html.parser import HTMLParser
import urllib.request
import re

class myHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('tag: ',tag)
    def handle_endtag(self,tag):
        print('etag: ',tag)
    def handle_data(self,data):
        print('data: ',data)

url = urllib.request.urlopen('http://gov.uk')
html = url.read()
html = str(html)
regex = re.compile('<title>(.+?)</title>')
print(regex.search(html).group(1))

##parser = myHTMLParser(strict=False)
##parser.feed(html)
