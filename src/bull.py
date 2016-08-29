from itertools import groupby

a = '1'
for i in range(0, 30):
	a = ''.join(str(len(list(v))) + k for k, v in groupby(a))

print len(a)