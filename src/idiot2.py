import httplib
import base64
import re
import zipfile
import StringIO

def getRange(left, right):
	conn = httplib.HTTPConnection('www.pythonchallenge.com')
	headers = {'Authorization': 'Basic ' + base64.b64encode('butter:fly'),
	'Range': 'bytes=' + left + '-' + right}
	conn.request('GET', '/pc/hex/unreal.jpg', '', headers)
	return conn.getresponse()

left = '30203'
right = '30204'

while True:
	res = getRange(left, right)
	print res.read(),
	if res.getheader('content-range') == None:
		break
	text = re.compile('(?<=-)[0-9]+(?=/)').findall(res.getheader('content-range'))
	left = str(int(text[0]) + 1)
	right = str(int(left) + 1)

left = '2123456789'
right = str(int(left) + 1)
res = getRange(left, right)
text = res.read()[:-1]
print text
print text[::-1]
pwd = 'invader'[::-1]
print pwd

text = re.compile('[0-9]+(?=-)').findall(res.getheader('content-range'))
left = str(int(text[0]) - 1)
right = str(int(left) + 1)
res = getRange(left, right)
text = res.read()
print text,

left = re.compile('[0-9]+').findall(text)[0]
right = str(int(left) + 1)
res = getRange(left, right)
src = res.read()

file = open('package.pack', 'w')
file.write(zipfile.ZipFile(StringIO.StringIO(src)).read('package.pack', pwd=pwd))
file.close()
print package.pack
