import urllib
import StringIO
import Image

src = urllib.urlopen('http://repeat:switch@www.pythonchallenge.com/pc/ring/bell.png').read()
im = Image.open(StringIO.StringIO(src))
im.load()

ret = list(im.split()[1].getdata())
diff = [abs(x - y) for x, y in zip(ret[0::2], ret[1::2])]
msg = filter(lambda x: x != 42, diff)
print ''.join([chr(x) for x in msg])

def whodunnit():
	return 'Guido van Rossum'

print whodunnit().split()[0]
