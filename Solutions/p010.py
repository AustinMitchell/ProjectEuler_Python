from __future__ import division
import math

def primeList(n):
    i = 1
    plist = [2]
    while i < n:
        i += 2
        valid = True
        for p in plist:
            if p > math.sqrt(i):
                break
            if i%p==0:
                valid = False
                break
        if valid:
            plist.append(i)
    return plist

print sum(primeList(2000000))