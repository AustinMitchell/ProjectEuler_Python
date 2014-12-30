from __future__ import division

coinVal = [200, 100, 50, 20, 10, 5, 2, 1]

def totalCombinations(remaining=200, minID=0):
	if remaining < 0:
		return 0
	elif remaining == 0:
		return 1
	else:
		total = 0
		for i in range(minID, 8):
			total += totalCombinations(remaining-coinVal[i], i)
		return total

print totalCombinations()
