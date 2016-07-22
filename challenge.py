# Problem 0 (http://www.pythonchallenge.com/pc/def/0.html)

pow(2, 38)

# Problem 1 (http://www.pythonchallenge.com/pc/def/map.html)

s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
a = maketrans('', '')[97:123]
b = list(a)
b.extend(['a', 'b'])
b.pop(0)
b.pop(0)
b = ''.join(b)
print s.translate(maketrans(a, b))

# Problem 2 (http://www.pythonchallenge.com/pc/def/ocr.html)

file = open('data1.txt')
s = file.read()
file.close()
ans = ''
for c in s:
	if c.isalpha():
		ans += c

print ans

# Problem 3 (http://www.pythonchallenge.com/pc/def/equality.html)

from re import findall
file = open('data2.txt')
s = file.read()
file.close()
print findall('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]', s)

# Problem 4 (http://www.pythonchallenge.com/pc/def/linkedlist.php)

import urllib
