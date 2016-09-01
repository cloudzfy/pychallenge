import Image
import urllib
import StringIO
import zipfile

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/maze.png').read()
im = Image.open(StringIO.StringIO(src))

black = (0, 0, 0, 255)
white = (255, 255, 255, 255)

for x in range(0, im.size[0]):
	if im.getpixel((x, 0)) == black:
		entrance = (x, 0)
	if im.getpixel((x, im.size[1] - 1)) == black:
		exit = (x, im.size[1] - 1)

move = {}
move[exit] = None
queue = [exit]
steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def checkBoundary(pos):
	return pos[0] >= 0 and pos[0] < im.size[0] and pos[1] >= 0 and pos[1] < im.size[1]

while len(queue) != 0:
	pos = queue.pop(0)
	if pos == entrance:
		break
	for s in steps:
		tmp = tuple(map(lambda x, y: x + y, pos, s))
		if checkBoundary(tmp) and not move.has_key(tmp) and im.getpixel(tmp) != white:
			queue.append(tmp)
			move[tmp] = pos

path = []
pos = entrance
while pos != exit:
	path.append(chr(im.getpixel(pos)[0]))
	pos = move[pos]

z = zipfile.ZipFile(StringIO.StringIO(''.join(path[1::2])))
Image.open(StringIO.StringIO(z.read('maze.jpg'))).show()

file = open('mybroken.zip', 'wb')
file.write(z.read('mybroken.zip'))
file.close()
print 'mybroken.zip'
