from math import sqrt

m = 2000000

def prime(p):
	if p % 2 == 0:
		return False
	sq = int(sqrt(p))
	i = 3
	while i <= sq:
		if p % i == 0:
			return False
		i = i + 2
	return True

p = 3
sum1 = 0
while p <= m:
	if prime(p):
		sum1 = sum1 + p
	p = p + 1

print (sum1 + 2)
