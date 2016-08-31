import urllib
import StringIO
import Image

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/white.gif').read()
im = Image.open(StringIO.StringIO(src))
ans = Image.new(im.mode, im.size)

path = []

while True:
	for x in range(0, im.size[0]):
		for y in range(0, im.size[1]):
			if im.getpixel((x, y)) != 0:
				path.append((x, y))
				break
	try:
		im.seek(im.tell() + 1)
	except EOFError:
		break

moves = [(path[i][0] - 100, path[i][1] - 100) for i in range(0, len(path))]

pos = (10, 100)
count = 0
ans.putpixel(pos, 255)
for m in moves:
	if m == (0, 0):
		pos = (10 + count * 40, 100)
		count += 1
	pos = tuple(map(lambda x, y: x + y, pos, m))
	ans.putpixel(pos, 255)

ans.show()
