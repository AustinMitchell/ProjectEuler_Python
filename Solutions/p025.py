from __future__ import division
import math

i = 2
fib = [1, 1]

while(len(str(fib[1]))<1000):
	i+= 1
	temp = fib[1]
	fib[1] = sum(fib)
	fib[0] = temp

print i