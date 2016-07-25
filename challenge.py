# Level 0 (http://www.pythonchallenge.com/pc/def/0.html)

pow(2, 38)

# Level 1 (http://www.pythonchallenge.com/pc/def/map.html)

from string import maketrans
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

from re import search
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
zip = zipfile.ZipFile('channel.zip','r')
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

# Level 9 (http://www.pythonchallenge.com/pc/return/good.html)

import Image

first = [146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399]

second = [156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136]

im = Image.new('RGB', (500, 500))
total = first + second
for i in range(0, len(total), 2):
	im.putpixel((total[i], total[i + 1]), (255, 255, 255))

im.show()

# Level 10 (http://www.pythonchallenge.com/pc/return/bull.html)

from itertools import groupby
s = '1'
for i in range(0, 30):
	s = ''.join(str(len(list(v))) + k for k, v in groupby(s))

print len(s)

# Level 11 (http://www.pythonchallenge.com/pc/return/5808.html)

import Image
im = Image.open('cave.jpg')
oddodd = Image.new(im.mode, im.size)
eveneven = Image.new(im.mode, im.size)
oddeven = Image.new(im.mode, im.size)
evenodd = Image.new(im.mode, im.size)
for x in range(0, im.size[0]):
	for y in range(0, im.size[1]):
		if x % 2 == 0 and y % 2 == 0:
			eveneven.putpixel((x / 2, y / 2), im.getpixel((x, y)))
		elif x % 2 == 0 and y % 2 == 1:
			evenodd.putpixel((x / 2, (y - 1) / 2), im.getpixel((x, y)))
		elif x % 2 == 1 and y % 2 == 0:
			oddeven.putpixel(((x - 1) / 2, y / 2), im.getpixel((x, y)))
		else:
			oddodd.putpixel(((x - 1) / 2, (y - 1) / 2), im.getpixel((x, y)))

oddodd.show()
eveneven.show()
oddeven.show()
evenodd.show()

# Level 12 (http://www.pythonchallenge.com/pc/return/evil.html)

file = open('evil2.gfx')
data = file.read()
file.close()
for i in range(0, 5):
	file = open('evil2-%d.jpg' % i, 'w')
	file.write(data[i::5])
	file.close()

# Level 13 (http://www.pythonchallenge.com/pc/return/disproportional.html)

import xmlrpclib
server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.system.methodHelp('phone')
print server.phone('Bert')

# Level 14 (http://www.pythonchallenge.com/pc/return/italy.html)

import Image
im = Image.file('wire.png')
ans = Image.new(im.mode, (100, 100))
step = [[1, 0], [0, 1], [-1, 0], [0, -1]]
maxLen = [[i, i - 1, i - 1, i - 2] for i in range(100, 1, -2)]
maxLen = reduce(lambda x, y: x + y, maxLen)
pos = [-1, 0]
s = 0
count = 0
for l  in maxLen:
	for i in range(l):
		pos = tuple(map(lambda x, y: x + y, pos, step[s]))
		ans.putpixel(pos, im.getpixel((count, 0)))
		count += 1
	s = (s + 1) % 4

ans.show()

# Level 15 (http://www.pythonchallenge.com/pc/return/uzi.html)

from calendar import isleap
from datetime import date
for year in range(1006, 1997, 10):
	d = date(year, 1, 1)
	if isleap(year) and d.weekday() == 3:
		print year

# Level 16 (http://www.pythonchallenge.com/pc/return/mozart.html)

import Image
im = Image.file('mozart.gif')
for y in range(im.size[1]):
	col = [im.getpixel((x, y)) for x in range(im.size[0])]
	idx = col.index(195)
	col = col[idx:] + col[:idx]
	[im.putpixel((x, y), col[x]) for x in range(im.size[0])]

# Level 17 (http://www.pythonchallenge.com/pc/return/romance.html)

import urllib
import urllib2
import cookielib
from re import search
import bz2

cookiejar = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(handler)

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
val = '44827'
info = 'B'
while True:
	data = opener.open(url + val).read()
	for c in cookiejar:
		if c.name == 'info':
			info += c.value
	print data
	print info
	try:
		val = search('[0-9]+', data).group()
	except:
		break

info = urllib.unquote_plus(info)
print bz2.decompress(info)

import xmlrpclib
server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.system.listMethods()
print server.system.methodHelp('phone')
print server.phone('Leopold')

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
cookie = cookielib.Cookie(version=0, name='info', value='the+flowers+are+on+their+way', port=None, port_specified=False, domain='.pythonchallenge.com', domain_specified=True, domain_initial_dot=True, path='/', path_specified=True, secure=False, expires=1470023979, discard=False, comment=None, comment_url=None, rest={}, rfc2109=False)
cookiejar = cookielib.CookieJar()
cookiejar.set_cookie(cookie)
handler = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(handler)
data = opener.open(url).read()

# Level 18 (http://www.pythonchallenge.com/pc/return/balloons.html)

from difflib import Differ
from binascii import unhexlify
file = open('deltas', 'r')
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

f1 = open('pic1.png', 'wb')
f1.write(unhexlify(pic1))
f1.close()
f2 = open('pic2.png', 'wb')
f2.write(unhexlify(pic2))
f2.close()
f3 = open('pic3.png', 'wb')
f3.write(unhexlify(pic3))
f3.close()
