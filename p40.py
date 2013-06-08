def getDigits(n):
	l = []
	while (n > 10):
		l.append(n % 10)
		n = n // 10
	if n == 10:
		l.append(0)
		l.append(1)
	else:
		l.append(n)
	l.reverse()
	return l

i = 2
length = 1
truth = True
prod = 1
l_max = 1000000
while truth:
	if length > l_max:
		truth = False
		break
	digits = getDigits(i)
	for digit in digits:
		length = length + 1
		#print digit, length, i
		if [1, 10, 100, 1000, 10000, 100000, 1000000].__contains__(length):
			print digit, length, i
			prod = prod * digit
	i = i + 1

print prod
print "---"
print 10370, getDigits(10370)
