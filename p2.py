def fib(n):
	l = []
	p = 1
	i = 2
	count = 2
	sum = 0
	while i < n:
		sum = sum + i
		i, p = 4 * i + p, i
	return sum

print fib(4000000)
