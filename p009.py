from __future__ import division

def makeAnswer():
	for a in range(1, 1001):
		for b in range(1, 1001):
			c = (a**2 + b**2)**0.5
			if c == round(c):
				if a + b + int(c) == 1000:
					return a * b * int(c)

print makeAnswer()