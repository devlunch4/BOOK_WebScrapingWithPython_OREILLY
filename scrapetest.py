from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.html)
print(bs.h1)

# bs = BeautifulSoup(html.read(), 'lxml')
# print('lxml', bs.html)
# print('lxml', bs.h1)
#
# bs = BeautifulSoup(html.read(), 'html5lib')
# print('html5lib', bs.html)
# print('html5lib', bs.h1)
