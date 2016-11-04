# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
import re
from BeautifulSoup import *

url = raw_input('Enter url - ')
count = raw_input('Enter count -')
count = int(count)
position = raw_input('Enter position -')
position = int(position)
html = urllib.urlopen('http://python-data.dr-chuck.net/known_by_Roos.html').read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
print tags[17]
name = []

# start tracing
for i in range(1,count + 1):
    if count > i:
        tags = soup('a')
        Tag = tags[position - 1]
        html_new = Tag.get('href', None)
        html = urllib.urlopen(html_new).read()
        soup = BeautifulSoup(html)
        print i,Tag

    elif count == i:
        tags = soup('a')
        Tag_in_use = tags[position - 1]
        html_new1 = Tag_in_use.get('href', None)
        name = re.findall('by_(.+)\.html',html_new1)
        print name
# hardest assignment ever!!!!!