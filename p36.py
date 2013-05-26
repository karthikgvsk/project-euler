# Problem 36
# Double Base Palindromes
# BRUTE FORCE!
# we can generate palindromes in a base and check in another

def getDigits(n):
	l = []
	while n > 10:
		l.append(n % 10)
		n = n // 10
		
	if n == 10:
		l.append(0)
		l.append(1)
	else:
		l.append(n)
	
	l.reverse()
	return l

def getBinDigits(n):
	l = []
	while n > 2:
		l.append(n % 2)
		n = n // 2
	if n == 2:
		l.append(0)
		l.append(1)
	else:
		l.append(n)
	
	l.reverse()
	return l

def isOddDigit(d):
	return [1, 3, 5, 7, 9].__contains__(d)

n = 1
N = 1000000
mainList = []
while n <= N:
	digits = getDigits(n)
	
	# some optimization 
	# THe number is odd so the starting digit should also be odd
	if not isOddDigit(digits[0]):
		n = n + 2
		continue
	
	binDigits = getBinDigits(n)
	#print digits, binDigits
	truth1 = True
	j = 0
	numDigits = len(digits)
	while j < numDigits and truth1:
		if digits[j] != digits[numDigits - 1 - j]:
			truth1 = False
			break
		j = j + 1

	truth2 = True
	j = 0
	numDigits = len(binDigits)
	while j < numDigits and truth2:
		if binDigits[j] != binDigits[numDigits - 1 - j]:
			truth2 = False
			break
		j = j + 1
	
	if truth1 and truth2:
		mainList.append(n)
	
	# consider only odd numbers because
	# starting binary digit is always 1
	# so to be palindromic in binary, 
	# the last digit shld also be 1
	n = n + 2

print mainList
print sum(mainList)	
