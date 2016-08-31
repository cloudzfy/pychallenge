import zlib
import bz2

file = open('package.pack', 'r')
package = file.read()
file.close()

log = ''

while True:
	if package[:2] == 'x\x9c':
		package = zlib.decompress(package)
		log += 'z'
	elif package[:2] == 'BZ':
		package = bz2.decompress(package)
		log += 'b'
	elif package[-2:] == '\x9cx':
		package = zlib.decompress(package[::-1])
		log += 'Z'
	elif package[-2:] == 'ZB':
		package = bz2.decompress(package[::-1])
		log += 'B'
	else:
		break

print package
print package[::-1]

print log.replace('z', ' ').replace('Z', '\n')