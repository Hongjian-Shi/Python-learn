import urllib
import xml.etree.ElementTree as ET

serviceurl = 'http://python-data.dr-chuck.net/comments_320262.xml '

raw_url = raw_input('Enter the url - ')
if len(raw_url) < 1:
    raw_url = serviceurl

xml_data = urllib.urlopen(raw_url).read()
comment_count = 0
tree = ET.fromstring(xml_data)
count = tree.findall('comments/comment')
for item in count:
    print item
    comment_count = int(item.find('count').text) + comment_count

print comment_count