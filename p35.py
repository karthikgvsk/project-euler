# PROBLEM #%: CIRCULAR PRIMES
from math import sqrt

def getDigits(n):
	l = []
	
	while n > 10:
		l.append(n % 10)
		n = n // 10

	if n == 10:
		l.append(1)
		l.append(0)
	else:
		l.append(n)
	l.reverse()
	return l

def eliminatePrime(prime):
	digits = getDigits(prime)
	l = [0, 2, 4, 5, 6, 8]
	for d in l:
		if digits.__contains__(d):
			return True
	return False


primeList = [2]
cirPrimeList = []
i = 3
n = 1000000 # 1 million

# first determining the prime list till 1 million
while i <= n:
	truth = True
	for j in primeList:
		if j > sqrt(n):
			break
		if i % j == 0:
			truth = False
			break
	if truth:
		primeList.append(i)

	i = i + 1

# determining the circular primes

for prime in primeList:
	if (not cirPrimeList.__contains__(prime)) and (not eliminatePrime(prime)):
		truth = True
		digits = getDigits(prime)	
		numDigits = len(digits)
		cirNums = []
		for i in range(numDigits):
			# forming a circular number
			digit1 = digits[0]
			del digits[0]
			digits.append(digit1)
			cirNum = 0
			for digit in digits:
				cirNum = 10 * cirNum + digit
				
			#if (not cirNums.__contains__(cirNum)) and (not cirPrimeList.__contains__(cirNum)):
			cirNums.append(cirNum)
			if not primeList.__contains__(cirNum):
				truth = False
				break
		
		if truth:
			cirPrimeList = cirPrimeList + cirNums

cirPrimeList.append(2)
cirPrimeList.append(5)
cirPrimeList.sort()
l = list(set(cirPrimeList))
l.sort()
print len(l)

