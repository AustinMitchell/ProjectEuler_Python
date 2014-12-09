from __future__ import division

# Naive but it works. Go away.
def isPrime(n):
	for i in range(2, n//2+1):
		if n%i == 0:
			return False
	return True

i = 1
p = 0
while (p < 10001):
	i += 1
	if isPrime(i):
		p += 1

print i