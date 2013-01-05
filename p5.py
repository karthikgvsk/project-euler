#smallest multiple
#2520 is the smallest number that can be divided by each of the numbers from#1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the#numbers from 1 to 20?

from math import log
def primelist(n):
	l = [0] * (n + 1)
	p = 2
	while p <= n:
		q = 2
		while q <= n // p:
			l[p * q] = 1
			q = q + 1
		p = p + 1
	l[0], l[1], l[2], l[3] = 1, 1, 0, 0
	return l

n = 20
l = primelist(n)
prod = 1
for i in range(len(l)):
	if l[i] == 0:
		power = int(log(n, i))
		prod = prod * (i ** power)
print prod

	
