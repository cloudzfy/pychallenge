import urllib
import StringIO
import Image

src = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg').read()
im = Image.open(StringIO.StringIO(src))
ans = Image.new(im.mode, im.size)

for x in range(0, im.size[0]):
	for y in range(0, im.size[1]):
		if x % 2 == 0 and y % 2 == 0:
			ans.putpixel((x, y), im.getpixel((x, y)))
		elif x % 2 == 1 and y % 2 == 1:
			ans.putpixel((x, y), im.getpixel((x, y)))

ans.show()