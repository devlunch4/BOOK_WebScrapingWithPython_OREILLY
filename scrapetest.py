from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print('html>>>', bs.html)
print()
print('h1>>>', bs.h1)
print()
print('head>>>', bs.head)
print()
print('div>>>', bs.div)
