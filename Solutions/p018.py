from __future__ import division
import math

f = open("input/p018.txt", "r")

tree = list(f)
for line in range(len(tree)):
	tree[line] = [int(s) for s in tree[line].split()]

for level in reversed(range(len(tree)-1)):
	for i in range(len(tree[level])):
		tree[level][i] = max(tree[level][i]+tree[level+1][i], tree[level][i]+tree[level+1][i+1])

print tree[0][0]
