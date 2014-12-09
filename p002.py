from __future__ import division

fib = [0, 1]
t = 0
while (fib[1] < 4000000):
	temp = fib[0] + fib[1]
	fib[0] = fib[1]
	fib[1] = temp
	if temp%2 == 0:
		t += temp

print t
