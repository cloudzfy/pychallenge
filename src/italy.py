import urllib
import Image
import StringIO

src = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/wire.png').read()
im = Image.open(StringIO.StringIO(src))
ans = Image.new(im.mode, (100, 100))
step = [[1, 0], [0, 1], [-1, 0], [0, -1]]
maxLen = [[i, i - 1, i - 1, i - 2] for i in range(100, 1, -2)]
maxLen = reduce(lambda x, y: x + y, maxLen)
idx = 0
stepIdx = 0
pos = (-1, 0)

for l  in maxLen:
	for i in range(l):
		pos = tuple(map(lambda x, y: x + y, pos, step[stepIdx]))
		ans.putpixel(pos, im.getpixel((idx, 0)))
		idx += 1
	stepIdx = (stepIdx + 1) % 4

ans.show()