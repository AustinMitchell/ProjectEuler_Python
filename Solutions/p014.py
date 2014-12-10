from __future__ import division
import math

def collatzChainSize(n):
	size = 1
	current = n
	while (current != 1):
		size += 1
		if current%2 == 0:
			current = current//2
		else:
			current = current*3 + 1
	return size

largest = [0, 0]
for i in range(1, 1000000):
	size = collatzChainSize(i)
	if size > largest[1]:
		largest[0] = i
		largest[1] = size

print largest[0]