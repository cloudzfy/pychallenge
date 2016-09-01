import urllib
import StringIO
import wave
import Image

src = [urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/lake%d.wav' % i).read() for i in range(1, 26)]

im = Image.new('RGB', (300, 300))

def getJigsaw(i):
	wav = wave.open(StringIO.StringIO(src[i]))
	return Image.fromstring('RGB', (60, 60), wav.readframes(wav.getnframes()))

def putJigsaw(i, pic):
	pos = (i % 5 * 60, i // 5 * 60)
	for x in range(0, 60):
		for y in range(0, 60):
			tmp = tuple(map(lambda a, b: a + b, pos, (x, y)))
			im.putpixel(tmp, pic.getpixel((x, y)))

for i in range(0, 25):
	putJigsaw(i, getJigsaw(i))

im.show()
