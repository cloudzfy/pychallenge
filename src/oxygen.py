import urllib
import StringIO
import Image
import re

src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png').read()
im = Image.open(StringIO.StringIO(src))
x = 0
y = 0
for i in range(0, im.size[1]):
	p = im.getpixel((0, i))
	if p[0] == p[1] == p[2]:
		y = i
		break

for i in range(0, im.size[0]):
	p = im.getpixel((i, y))
	if not p[0] == p[1] == p[2]:
		x = i
		break

text = []
for i in range(0, x, 7):
	p = im.getpixel((i, y))
	text.append(chr(p[0]))

ret = re.compile('[0-9]+').findall(''.join(text))
ans = [chr(int(x)) for x in ret]
print ''.join(ans)
