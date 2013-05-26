# Digit factorials
# upper bound is important
from math import log

def getDigits(num):
	l = []
	while num > 10:
		l.append(num % 10)
		num = num // 10
	if num == 10:
		l.append(1)
		l.append(0)
	else:
		l.append(num)
	return l

# producing the factorial list
factList = [1]
i = 1
prod = 1
while i <= 9:
	prod = prod * i
	factList.append(prod)
	i = i + 1

# taking the right numbers
num = 1
LARGE = 2 * log(factList[9]) * factList[9]
mainList = []
stop = False
while not stop: #num <= LARGE:
	digits = getDigits(num)
	sum1 = 0
	for digit in digits:
		sum1 = sum1 + factList[digit]
	if num == sum1:
		mainList.append(num)
	num = num + 1
	nineFactorial = factList[9]
	if num > nineFactorial * log(num):
		stop = True

print mainList
print factList
print sum(mainList)
print "you should subtract 3 from the sum"
print "since cases 1 and 2 are not to be included"
