from __future__ import division
import math
# Found this online, I don't actually know how the normal algorithm works, and I can't read this either.
def atkinsPrimeList(limit=1000000):
    '''use sieve of atkins to find primes <= limit.'''
    primes = [0] * limit
 
    # n = 3x^2 + y^2 section
    xx3 = 3
    for dxx in xrange( 0, 12*int( math.sqrt( ( limit - 1 ) / 3 ) ), 24 ):
        xx3 += dxx
        y_limit = int(12*math.sqrt(limit - xx3) - 36)
        n = xx3 + 16
        for dn in xrange( -12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]
 
        n = xx3 + 4
        for dn in xrange( 12, y_limit + 1, 72 ):
            n += dn
            primes[n] = not primes[n]
 
    # n = 4x^2 + y^2 section
    xx4 = 0
    for dxx4 in xrange( 4, 8*int(math.sqrt((limit - 1 )/4)) + 4, 8 ):
        xx4 += dxx4
        n = xx4+1
 
        if xx4%3:
            for dn in xrange( 0, 4*int( math.sqrt( limit - xx4 ) ) - 3, 8 ):
                n += dn
                primes[n] = not primes[n]
 
        else:
            y_limit = 12 * int( math.sqrt( limit - xx4 ) ) - 36
 
            n = xx4 + 25
            for dn in xrange( -24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]
 
            n = xx4+1
            for dn in xrange( 24, y_limit + 1, 72 ):
                n += dn
                primes[n] = not primes[n]
 
    # n = 3x^2 - y^2 section
    xx = 1
    for x in xrange( 3, int( math.sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx
 
        if n > limit:
            min_y = ((int(math.sqrt(n - limit))>>2)<<2)
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4
 
        else:
            s = 4
 
        for dn in xrange( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]
 
    xx = 0
    for x in xrange( 2, int( math.sqrt( limit / 2 ) ) + 1, 2 ):
        xx += 4*x - 4
        n = 3*xx
 
        if n > limit:
            min_y = ((int(math.sqrt(n - limit))>>2)<<2)-1
            yy = min_y*min_y
            n -= yy
            s = 4*min_y + 4
 
        else:
            n -= 1
            s = 0
 
        for dn in xrange( s, 4*x, 8 ):
            n -= dn
            if n <= limit and n%12 == 11:
                    primes[n] = not primes[n]
 
    # eliminate squares        
    for n in xrange(5,int(math.sqrt(limit))+1,2):
        if primes[n]:
            for k in range(n*n, limit, n*n):
                primes[k] = False
 
    return [2,3] + filter(primes.__getitem__, xrange(5,limit,2))

primeList = atkinsPrimeList()

def generatePrimeFactors(n):
	current = n
	primeFactors = dict()
	for p in primeList:
		if current == 1:
			break
		while(current%p==0):
			current = current//p
			if not p in primeFactors:
				primeFactors[p] = 1
			else:
				primeFactors[p] += 1
	return primeFactors

def generateFactor(primeList, occuranceList):
	return reduce(lambda x, y: x*y, [primeList[i]**occuranceList[i] for i in range(len(primeList))])

def pushOccuranceList(olist, maxolist):
	current = 0
	while(True):
		olist[current] += 1
		if olist[current] > maxolist[current]:
			if current+1 >= len(maxolist):
				return False
			olist[current] = 0
			current+= 1
		else:
			break
	return True

def factorList(n):
	primeFactorList = generatePrimeFactors(n)

	plist = sorted([key for key in primeFactorList])
	maxOccuranceList = [primeFactorList[key] for key in plist]
	occuranceList = [0 for i in plist]
	factorList = set()

	while(True):
		valid = pushOccuranceList(occuranceList, maxOccuranceList)
		if not valid:
			break
		else:
			factorList.add(generateFactor(plist, occuranceList))

	factorList.remove(n)
	factorList.add(1)
	return factorList

total = 0
factorSum = [0, 0]+[sum(factorList(i)) for i in range(2, 10000)]
for i in range(len(factorSum)):
	if factorSum[i] < 10000:
		if i == factorSum[factorSum[i]] and i != factorSum[i]:
			print str(i) + ": " + str(factorSum[i])
			total += i

print total