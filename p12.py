from __future__ import division

def sumAll(n):
	return n*(n+1)//2

def divisors(n):
	total = 2
	for i in range(2, n//2+1):
		if n//i == n/i:
			total += 1
	return total

s = 0
d = 0
i = 1
while(d<=500):
	s = sumAll(i)
	d = divisors(s)
	i+=1
	if i % 500 == 0:
		print "*"

print s