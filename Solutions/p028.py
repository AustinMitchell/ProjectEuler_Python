from __future__ import division

current = 1
total = 1
step = 2

while step <= 1000:
	for i in range(4):
		current += step
		total += current
	step += 2

print total