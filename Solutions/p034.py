from __future__ import division

def factorial(n):
	if n <= 1:
		return 1
	else:
		return reduce(lambda x, y: x*y, range(1, n+1))
digitFac = [factorial(i) for i in range(0, 10)]