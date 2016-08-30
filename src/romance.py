import urllib
import urllib2
import cookielib
import re
import bz2
import xmlrpclib

cookiejar = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookiejar)
opener = urllib2.build_opener(handler)

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing='
num = '12345'
info = []

while True:
	src = opener.open(url + num).read()
	print src
	info.append(list(cookiejar)[0].value)
	text = re.compile('[0-9]+').findall(src)
	if len(text) == 0:
		break
	else:
		num = text[-1]

print bz2.decompress(urllib.unquote_plus(''.join(info)))

server = xmlrpclib.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print server.phone('Leopold')

url = 'http://www.pythonchallenge.com/pc/stuff/violin.php'
list(cookiejar)[0].value = 'the+flowers+are+on+their+way'
print opener.open(url).read()
