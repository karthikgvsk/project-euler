# amicable numbers problem
# used sieve of primes, sum property from prime factorization, and 
from math import sqrt
n = 10001

def primeList(n):
	l = [0] * (n + 1)
	i = 2
	while i < n:
		j = 2
		while j < (n // i):
			l[i * j] = 1
			j = j + 1
		i = i + 1
	l[0] = 1
	l[1] = 1
	return l

def divSum(n, l):
	i = 2
	prod = 1
	while i <= n:
		if l[i] == 0:
			sum1 = 0
			m = n
			while m > 0:
				if m % i != 0:
					break
				sum1 = sum1 + 1
				m = m // i
			#print i, sum1
			prod = prod * (((i ** (sum1 + 1)) - 1) // (i - 1))
		i = i + 1
	return prod
			


l1 = primeList(n)

l3 = [1] * n
i = 2
while i < n:
	if l1[i] != 0:
		l3[i] = divSum(i, l1) - i
	i = i + 1

l4 = []
looked = [False] * n
i = 2
while i < n:
	if not looked[i]:
		num1 = l3[i]
		looked[i] = True
		num2 = 0
		if num1 < n and num1 != i:
			num2 = l3[num1]
			looked[num1] = True
			if num2 == i:
				l4.append(i)
				l4.append(num1)
	i = i + 1
print l4
print sum(l4)
	
