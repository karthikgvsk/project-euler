# Truncatable primes
from math import sqrt
global fAndLDig 
fAndLDig= [2, 3, 5, 7]
mainList = []

def isPrime(n):
	if n == 1:
		return False

	i = 2
	while i <= int(sqrt(n)):
		if n % i == 0:
			return False
		i = i + 1

	return True

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

def listToNum(l):
	s = map(str, l)
	s = ''.join(s)
	s = int(s)
	return s

def checkTruncPrime(n, mainList):
	#print "++++++++++++++++++++++++++"
	#print n

	digits = getDigits(n)
	digitscopy = getDigits(n)
	
	if (not fAndLDig.__contains__(digits[0])) and \
		(not fAndLDig.__contains__(digits[-1])):
		return

	# check for forward removal
	forwNum = listToNum(digits[1:])
	backNum = listToNum(digits[:-1])
	#print "checking forNum and vackNum : ", forwNum, backNum
	if (not mainList.__contains__(forwNum)) or \
		(not mainList.__contains__(backNum)):
		
		# check for forward case
		truth1 = True
		digits = digits[1:]
		while len(digits) > 0:
			#print digits
			num = listToNum(digits)
			if not isPrime(num):
				truth1 = False
				break
			digits = digits[1:]
		
		# check for reverse case
		truth2 = True
		digitscopy = digitscopy[:-1]
		while len(digitscopy) > 0:
			num = listToNum(digitscopy)
			if not isPrime(num):
				truth2 = False
				break
			digitscopy = digitscopy[:-1]
	
		if truth1 and truth2:
			mainList.append(n)
	else:
		mainList.append(n)
	
	#print "++++++++++++++++++++++++++++++"

n = 23
while True:
	if isPrime(n) and not mainList.__contains__(n):
		checkTruncPrime(n, mainList)
		
	if len(mainList) >= 11:
		break

	n = n + 2

print mainList
print sum(mainList)
