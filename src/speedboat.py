import urllib
import Image
import StringIO
from string import maketrans
import bz2

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/zigzag.gif').read()
im = Image.open(StringIO.StringIO(src))

mfrom = ''.join([chr(i) for i in range(256)])
mto = ''.join([chr(i) for i in im.getpalette()[::3]])
origin = im.tostring()
trans = origin.translate(maketrans(mfrom, mto))

delta = filter(lambda x: x[0] != x[1], zip(origin[1:], trans[:-1]))

ret = ''.join([''.join(delta[i]) for i in range(len(delta))])
text = bz2.decompress(ret[0::2])
print list(set(filter(lambda x: not keyword.iskeyword(x), text.split(' '))))

#####

delta = filter(lambda x: x[0] == x[1], zip(origin[1:], trans[:-1]))
ret = ''.join([''.join(delta[i]) for i in range(len(delta))])
pic = Image.new('1', im.size, 0)
pic.putdata(delta)
pic.show()