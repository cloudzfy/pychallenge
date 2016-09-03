import urllib
import StringIO
import Image

src = urllib.urlopen('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/mandelbrot.gif').read()
im = Image.open(StringIO.StringIO(src))

