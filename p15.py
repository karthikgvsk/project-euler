from math import sqrt

def isPrime(p):
	if p % 2 == 0:
		return False
	i = 3
	while i <= int(sqrt(p)):
		if p % i == 0:
			return False
		i = i + 2
	return True

def sieve(n):
	l = [0] * (n + 1)
	l[0] = 1
	l[1] = 1
	i = 2
	while i <= n:
		j = 2
		while j <= (n // i):
			if i * j <= n:
				l[i * j] = 1
			j = j + 1
		i = i + 1
	return l

prime_list = sieve(500000)
def numOfFacts(n, even):
	#prime_list = sieve(n)
	#print prime_list
	if prime_list[n] == 0:
		return 2
	prod = 1
	i = 2
	while i <= n:
		if prime_list[i] == 0:
			sum1 = 0
			p = i
			while(n % i == 0):
				sum1 = sum1 + 1
				n = n / i
			if i == 2:
				if even:
					prod = prod * sum1
				else:
					prod = prod * (sum1 + 1)
			else:
				prod = prod * (sum1 + 1)
		i = i + 1
	return prod
	

def divCount(n):
	i = 1
#	count = 0
#	while i <= n:
#		if n % i == 0:
#			count = count + 1
#		i = i + 1
#	return count
#
n = 100
max1 = 0
while True:
	num = n * (n + 1) // 2
	even = False
	if n % 2 == 0:
		even = True
	num1 = numOfFacts(n, even)
	num2 = numOfFacts(n + 1, not even)
	#print n
	#print num1 * num2
	#print "============="
	if num1 * num2 >= 500:
		print n
		print num1 * num2
		print n * (n + 1) // 2
		break
	if max1< num1 * num2:
		max1 = num1 * num2
		print max1
	n = n + 1

