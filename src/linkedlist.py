import urllib
import re

stack = ['12345']

while True:
	num = stack.pop()
	src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num).read()
	print src
	text = re.compile('[0-9]+').findall(src)
	if len(text) == 0:
		if src == 'Yes. Divide by two and keep going.':
			stack.append(str(int(num) / 2))
		else:
			break
	else:
		stack.append(text[-1])
