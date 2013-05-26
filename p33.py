# digit cancelling fractions

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

l = []
count = 0
for a in range(1, 10):
	for c in range(1, 10):
		for d in range(1, 10):
			num1 = 10 * a + c
			den1 = 10 * c + d
			num2 = a
			den2 = d
			if num1 < den1 and num1 * den2 == num2 * den1:
				l.append((a, c, d))
				count = count + 1
			if count == 4:
				break
		if count == 4:
			break
	if count == 4:
		break

num = 1
den = 1
for val in l:
	num = num * val[0]
	den = den * val[2]
g = gcd(num, den)
print den / g
