from __future__ import division
import math

numsAndTeens = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
				"thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen")
tenNames = ("ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "twenty")

def numLetters(n):
	hundreds = n//100
	tens = n%100

	total = 0
	if hundreds > 0:
		total += len(numsAndTeens[hundreds-1]) + len("hundred")
		#print numsAndTeens[hundreds-1] + " hundred "
		if tens != 0:
			total += 3
			#print "and "
	if tens != 0:
		if tens <= 19:
			total += len(numsAndTeens[tens-1])
			#print numsAndTeens[tens-1]
		else:
			total += len(tenNames[tens//10-1])
			#print tenNames[tens//10-1] + " "
			if tens%10 != 0:
				total += len(numsAndTeens[tens%10-1])
				#print numsAndTeens[tens%10-1]

	return total

print sum([numLetters(i) for i in range(1, 1000)]) + 11