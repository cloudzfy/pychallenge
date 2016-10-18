import urllib

BLANK   = ' '
FILLED  = '#'
UNKNOWN = '?'

def solver(url):
	src = urllib.urlopen(url).readlines()
	index = -1
	dim = []
	horizontal = []
	vertical = []
	file = [dim, horizontal, vertical]
	for line in src:
		if line[0] == '\n':
			continue
		elif line[0] == '#':
			index += 1
		else:
			file[index].append([int(x) for x in line.replace('\n', '').split(' ')])

	optH = [generateOpt(i, dim[0][0]) for i in horizontal]
	optV = [generateOpt(i, dim[0][1]) for i in vertical]
	opt = [optH, optV]
	optIdx = 0
	solution = [[UNKNOWN for i in range(dim[0][0])] for j in range(dim[0][1])]

	while not isSolved(solution):
		for i in range(len(opt[optIdx])):
			opt[optIdx][i] = filter(lambda x: dataMatch(x, solution[i]), opt[optIdx][i])
			updateSolution(solution, i, solve(opt[optIdx][i]))
		optIdx = (optIdx + 1) % 2
		solution = transpose(solution)

	if optIdx == 1:
		solution = transpose(solution)

	printSolution(solution)

def generateOpt(data, size):
	if len(data) == 1:
		return [BLANK * i + FILLED * data[0] + BLANK * (size - i - data[0]) for i in range(size - data[0] + 1)]
	else:
		return [BLANK * i + FILLED * data[0] + BLANK + j for i in range(size - sum(data) - len(data) + 2) \
			for j in generateOpt(data[1:], size - i - data[0] - 1)]

def dataMatch(candidate, pattern):
	for i in range(len(pattern)):
		if pattern[i] <> UNKNOWN and pattern[i] <> candidate[i]:
			return False
	return True

def transpose(solution):
	return map(lambda *x: list(x), *solution)

def isSolved(solution):
	return reduce(lambda i, j: i and not UNKNOWN in j, solution, True)

def solve(candidates):
	return [UNKNOWN if len(i) > 1 else i.pop() for i in [set(j) for j in transpose(candidates)]]

def updateSolution(solution, idx, candidates):
	for i in range(len(candidates)):
		if candidates[i] <> UNKNOWN:
			solution[idx][i] = candidates[i]

def printSolution(solution):
	for s in solution:
		print ''.join(s)

print 'warmup.txt'
solver('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/warmup.txt')

print 'up.txt'
solver('http://kohsamui:thailand@www.pythonchallenge.com/pc/rock/up.txt')

