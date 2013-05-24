# Number spiral diagonal problem
# used mathematical simplification (solved the sqeuence)

n = 1001
i = 3
sum1 = 0
while i <= n:
	sum1 = sum1 + 4 * (i **2) - 6 * (i - 1)
	i = i + 2
print sum1 + 1
