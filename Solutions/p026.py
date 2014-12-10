from __future__ import division
import math

def chainLength(n):
	ten = 10
	while(n>ten):
		ten *= 10 

	previous = set()

	remainder = 0
	current = ten
	while(True):
		remainder = current%n
		if remainder == 0:
			return 0
		else:
			if (remainder, current) in previous:
				start = (remainder, current)
				current = remainder*ten
				length = 0
				while(True):
					remainder = current%n
					length += 1
					if remainder == start[0] and current == start[1]:
						return length
					current = remainder*ten

			else:
				previous.add((remainder, current))
				current = remainder*ten

largest = [0, 0]
for i in range(2, 1000):
	length = chainLength(i)
	if length > largest[1]:
		largest = [i, length]

print largest