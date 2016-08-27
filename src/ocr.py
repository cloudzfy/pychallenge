import urllib
import re

src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read()
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(src)[-1]
count = {}

for c in text:
	count[c] = count.get(c, 0) + 1

print ''.join(re.findall('[a-z]', text))