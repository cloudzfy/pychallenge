import urllib
import StringIO
import Image

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif').read()
im = Image.open(StringIO.StringIO(src))

for x in range(0, im.size[0]):
	for y in range(0, im.size[1]):
		if im.getpixel((x, y)) != 0:
			print x, y, im.getpixel((x, y))

