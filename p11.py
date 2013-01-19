def powOf2(n):
	if n == 0:
		return 1
	if n == 1:
		return 2
	if n % 2 == 0:
		return powOf2(n / 2) ** 2
	else:
		return powOf2(n // 2) ** 2 * 2

p = powOf2(1000)
sum = 0
while p > 0:
	sum = sum + (p % 10)
	p = p // 10
print sum


