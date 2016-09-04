import urllib
import StringIO
import Image
from math import sqrt

src = urllib.urlopen('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/mandelbrot.gif').read()
im = Image.open(StringIO.StringIO(src))

left = 0.34
top = 0.57
width = 0.036
height = 0.027

iteration = 128

xStep = width / im.size[0]
yStep = height / im.size[1]

ret = []

for y in range(im.size[1] - 1, -1, -1):
	for x in range(0, im.size[0]):
		c = complex(left + x * xStep, top + y * yStep)
		z = 0 + 0j
		for i in range(iteration):
			z = z * z + c
			if abs(z) > 2:
				break
		ret.append(i)

diff = [x - y for x, y in zip(list(im.getdata()), ret) if x != y]

size = [(x, len(diff) / x) for x in range(2, int(sqrt(len(diff))) + 1) if len(diff) % x == 0]

ans = Image.new('L', size[0])
ans.putdata([0 if x < 0 else 255 for x in diff])
ans.show()
