import urllib
import Image
import StringIO

src = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/mozart.gif').read()
im = Image.open(StringIO.StringIO(src))

for y in range(0, im.size[1]):
	col = [im.getpixel((x, y)) for x in range(0, im.size[0])]
	idx = col.index(195)
	col = col[idx:] + col[:idx]
	[im.putpixel((x, y), col[x]) for x in range(0, im.size[0])]

im.show()