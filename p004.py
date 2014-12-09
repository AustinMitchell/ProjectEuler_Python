from __future__ import division

def isPalindrome(s):
	for i in range(0, len(s)//2):
		if not s[i] == s[-i-1]:
			return False
	return True

largest = 0
for i in range(1, 1000):
	for j in range(1, 1000):
		if (isPalindrome(str(i*j)) and i*j > largest):
			largest = i*j

print largest
