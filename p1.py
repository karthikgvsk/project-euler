
def seqSum(target, n):
	p = target // n
	return n * p * (p + 1) // 2

print seqSum(999, 3) + seqSum(999, 5) - seqSum(999, 15)
