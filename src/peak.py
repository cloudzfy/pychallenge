import urllib
import pickle

src = urllib.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
data = pickle.load(src)
for line in data:
	print ''.join(x[0] * x[1] for x in line)
