from __future__ import division
import math

def factorial(n):
	return reduce(lambda x, y: x*y, range(1, n+1))

def choose(n, r):
	return factorial(n) // (factorial(r) * factorial(n-r))

print choose(40, 20)