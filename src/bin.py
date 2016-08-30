import urllib
import re

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html').read()
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->').findall(src)[0]
