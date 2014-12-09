from __future__ import division

# Finds the greatest common denominator between two integers
def gcd(a_, b_):
	a = a_
	b = b_
	while b != 0:
		r = a%b
		a = b
		b = r
	return a

# With these numbers you can make all numbers from 2 to 20
# e.g.: x%2=0 and x%5==0 <--> x%10==0
nums = (2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19)

# This finds the lowest common multiple for a set of numbers
print reduce (lambda x, y: (x*y) // gcd(x, y), nums)