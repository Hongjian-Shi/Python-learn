# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen('http://python-data.dr-chuck.net/comments_320265.html').read()
fh = urllib.urlopen('http://python-data.dr-chuck.net/comments_320265.html')

Num = []
for line in fh :
    if re.search('>([0-9]+)<',line):
        num = re.findall('>([0-9]+)<',line)
        for single in num:
            Num.append(single)

sum = int()
for num_str in Num:
    num_int = int(num_str)
    sum = num_int + sum

print sum