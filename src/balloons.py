import urllib
import StringIO
import gzip
from difflib import Differ
from binascii import unhexlify
import Image

src = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/deltas.gz').read()
file = gzip.GzipFile(fileobj=StringIO.StringIO(src))

left = []
right = []

for line in file.readlines():
	left.append(line[0:53])
	right.append(line[56:109])

file.close()

d = Differ()
result = list(d.compare(left, right))
pic1 = ''
pic2 = ''
pic3 = ''
for line in result:
	if line[0] == ' ':
		pic1 += line[1:].replace(' ', '').replace('\n', '')
	elif line[0] == '+':
		pic2 += line[1:].replace(' ', '').replace('\n', '')
	elif line[0] == '-':
		pic3 += line[1:].replace(' ', '').replace('\n', '')

Image.open(StringIO.StringIO(unhexlify(pic1))).show()
Image.open(StringIO.StringIO(unhexlify(pic2))).show()
Image.open(StringIO.StringIO(unhexlify(pic3))).show()
