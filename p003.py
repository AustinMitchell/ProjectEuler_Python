from __future__ import division

def isPrime(n):
	for i in range(2, n//2):
		if n%i == 0:
			return False
	return True

largest = 0
n = 600851475143   
current = 2
while (n != 1):
	if (n%current == 0):
		n = n//current
		if current > largest:
			largest = current
			current = 2
	else:
		current += 1
		while (not isPrime(current)):
			current += 1

print largest
