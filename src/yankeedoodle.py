import urllib
import Image
from math import sqrt

src = urllib.urlopen('http://repeat:switch@www.pythonchallenge.com/pc/ring/yankeedoodle.csv').read()
data = src.replace('\n', '').replace(' ', '').split(',')

size = [(x, len(data) / x) for x in range(2, int(sqrt(len(data))) + 1) if len(data) % x == 0]
im = Image.new('F', size[0])
im.putdata([float(x) for x in data], 256)
im = im.transpose(Image.ROTATE_90)
im = im.transpose(Image.FLIP_TOP_BOTTOM)
im.show()

msg = [int(data[i][5] + data[i + 1][5] + data[i + 2][6]) for i in range(0, len(data) - 2, 3)]
print ''.join([chr(x) for x in msg])