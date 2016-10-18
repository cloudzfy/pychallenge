import urllib
import StringIO
import Image
from math import sqrt

src = urllib.urlopen('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/beer2.png').read()
im = Image.open(StringIO.StringIO(src))

data = im.getdata()
ans = []

for i in range(len(set(data))):
	light = max(list(data))
	data = [255 if x == light else x for x in data]
	l = int(sqrt(len(data)))
	if l * l == len(data):
		tmp = Image.new(im.mode, (l, l))
		tmp.putdata(data)
		ans.append(tmp)
	data = filter(lambda x: x < light, list(im.getdata()))

idx = [16, 18, 22, 23, 25, 27, 28, 30]
for i in idx:
	ans[i].show()
