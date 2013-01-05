#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

from math import sqrt

n = 600851475143
i = int(sqrt(n))

l = [0] * (i + 2)

p = 2

while p <= (i // 2 + 1):
	q = 2
	while q <= (i // p):
		l[p * q] = 1
		q = q + 1
	p = p + 1

while i > 0:
	if n % i == 0 and l[i] == 0:
		print i
		break
	i = i - 1

