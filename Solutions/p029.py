from __future__ import division

items = set()

for i in range(2, 101):
	for j in range(2, 101):
		items.add(i**j)

print len(items)