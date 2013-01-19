# self powers problem
n = 10 ** 10
i = 1
sum1 = 0
while i <= 1000:
	j = 1
	prod = 1
	while j <= i:
		prod = prod * i % n
		j = j + 1
	sum1 = (sum1 + prod) % n
	i = i + 1
print sum1
