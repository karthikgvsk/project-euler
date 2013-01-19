
def fact(n):
	if n == 1:
		return 1
	if n == 0:
		return 1
	return n * fact(n - 1)

sum1 = 0
fac = fact(100)
while fac > 0:
	sum1 = sum1 + fac % 10
	fac = fac // 10
print sum1
