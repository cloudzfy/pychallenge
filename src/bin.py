import urllib
import re
from email.parser import parser

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/bin.html').read()
text = re.compile('<!--((?:[^-]+|-[^-]|--[^>])*)-->').findall(src)[0]
