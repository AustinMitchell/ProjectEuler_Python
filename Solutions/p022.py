from __future__ import division
import math

f = open("input/p022.txt", "r")
n = [[name.replace("\"", "") for name in line.split(",")] for line in list(f)]
names = []
for line in n:
	names.extend(line)

names = sorted(names)

score = 0
for n in range(len(names)):
	score += sum([ord(c)-64 for c in names[n]])*(n+1)

print score
