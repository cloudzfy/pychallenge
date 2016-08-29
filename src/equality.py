import urllib
import re

src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read()
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->', re.S).findall(src)[0]
print ''.join(re.compile('(?<=[^A-Z][A-Z]{3})[a-z]{1}(?=[A-Z]{3}[^A-Z])', re.S).findall(text))