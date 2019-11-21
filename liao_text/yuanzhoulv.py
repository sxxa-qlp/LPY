import itertools
def pi(N):
	p, c = 0, 1
	for si in itertools.takewhile(lambda x: x <= 2 * N - 1, itertools.count(1,2)):
		p, c = p + c * 4 / si, -c
	return p
print(pi(1000))