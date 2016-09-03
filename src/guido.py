import urllib
import bz2

src = urllib.urlopen('http://repeat:switch@www.pythonchallenge.com/pc/ring/guido.html').read()
msg = [len(line) for line in src.split('\n')[12:]]
print bz2.decompress(''.join([chr(x) for x in msg]))
