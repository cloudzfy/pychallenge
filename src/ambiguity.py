import Image
import urllib
import StringIO

src = urllib.urlopen('http://butter:fly@www.pythonchallenge.com/pc/hex/maze.png').read()
im = Image.open(StringIO.StringIO(src))

