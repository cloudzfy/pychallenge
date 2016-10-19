import urllib
import zipfile
import StringIO
import re

src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()
zip = zipfile.ZipFile(StringIO.StringIO(src))
num = '90052'
ans = []

while True:
	text = zip.read(num + '.txt')
	comment = zip.getinfo(num + '.txt').comment
	ans.append(comment)
	ret = re.compile('[0-9]+').findall(text)
	if len(ret) == 0:
		break
	else:
		num = ret[0]

print ''.join(ans)
