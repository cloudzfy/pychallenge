# Level 0 (http://www.pythonchallenge.com/pc/def/0.html)

pow(2, 38)

# Level 1 (http://www.pythonchallenge.com/pc/def/map.html)

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = maketrans('', '')[97:123]
b = list(a)
b.extend(['a', 'b'])
b.pop(0)
b.pop(0)
b = ''.join(b)
print s.translate(maketrans(a, b))

# Level 2 (http://www.pythonchallenge.com/pc/def/ocr.html)

file = open('data1.txt')
s = file.read()
file.close()
ans = ''
for c in s:
	if c.isalpha():
		ans += c

print ans

# Level 3 (http://www.pythonchallenge.com/pc/def/equality.html)

from re import findall
file = open('data2.txt')
s = file.read()
file.close()
print findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', s)

# Level 4 (http://www.pythonchallenge.com/pc/def/linkedlist.php)

import urllib
nothing = '12345'
for i in range (0, 400):
	file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
	data = file.readline()
	nothing = search('[0-9]+', data).group()
	print nothing

nothing = '8022'
for i in range (0, 400):
	file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
	data = file.readline()
	nothing = search('[0-9]+', data).group()
	print nothing

nothing = '63579'
for i in range (0, 400):
	file = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + nothing)
	data = file.readline()
	nothing = search('[0-9]+', data).group()
	print nothing

# Level 5 (http://www.pythonchallenge.com/pc/def/peak.html)

file = open('banner.txt','r')
data = pickle.load(file)
file.close()
for line in data:
	print ''.join(x[0]*x[1] for x in line)

# Level 6 (http://www.pythonchallenge.com/pc/def/channel.html)

nothing = '90052'
for i in range(0, 1000):
	file = open('channel/' + nothing + '.txt')
	data = file.readline()
	nothing = search('[0-9]+', data).group()
	print nothing

import zipfile
nothing = '90052'
file = zipfile.ZipFile('channel.zip','r')
ans = ''
for i in range(0, 1000):
	file = open('channel/' + nothing + '.txt')
	ans += zip.getinfo(nothing + '.txt').comment
	data = file.readline()
	file.close()
	nothing = search('[0-9]+', data).group()
print ans

# Level 7 (http://www.pythonchallenge.com/pc/def/oxygen.html)
import Image
im = Image.open('oxygen.png')
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
ans = ''
for i in range(0, x, 7):
	p = im.getpixel((i, y))
	ans += chr(p[0])
print ans

data = [105, 110, 116, 101, 103, 114, 105, 116, 121]
ans = ''
for c in data:
	ans += chr(c)
print ans

# Level 8 (http://www.pythonchallenge.com/pc/def/integrity.html)

import bz2
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
print bz2.decompress(un)
print bz2.decompress(pw)

