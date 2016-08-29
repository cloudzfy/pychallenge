import urllib

src = urllib.urlopen('http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx').read()

types = ['jpg', 'png', 'gif', 'png', 'jpg']
for i in range(0, 5):
	open('evil2-%d.%s' % (i, types[i]), 'w').write(src[i::5])
