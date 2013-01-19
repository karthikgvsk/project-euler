#a, b, c - pythogarean triplet c>= a, b
#a + b + c = 1000
#find a * b * c

#from some reductions, 500 >= c >= 413
#and 2000(a + b) -2ab - 1000^2 = 0

from math import sqrt
n = 100000
n1 = n / 2
n2 = int((sqrt(2) - 1) * n)

for c in range(n2, n1 + 1):
	for b in range(1, c):
		a = 1000 - b - c
		if a <= 0:
			continue
		if a**2 + b**2 == c**2:
			print a * b * c
			print a
			print b
			print c
			break
