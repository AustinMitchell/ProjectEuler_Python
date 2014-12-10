from __future__ import division
import math

def factorial(n):
	if n<= 1:
		return 1
	else:
		return reduce(lambda x, y: x*y, range(1, n+1))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = ""

currentSize = 1000000
i = 0
while(len(numbers) != 0):
	print numbers
	f = factorial(len(numbers)-1)
	if f < currentSize:
		currentSize -= f
		i += 1
	else:
		result += str(numbers[i])
		del numbers[i]
		i = 0

print result
