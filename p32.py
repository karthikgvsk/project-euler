# BRUTE FORCE !!!

def getDigits(n):
	l = []
	while n > 10:
		l.append(n % 10)
		n = n // 10
	if n == 10:
		l.append(1)
		l.append(0)
	else:
		l.append(n)
	return l

#f = open('p32.out', 'w')
gl = []
nl = []

for a in range(0, 10):
	for b in range(0, 10):
		for c in range(0, 10):
			for d in range(0, 10):
				for e in range(0, 10):
					
					# ab * cde format
					num1 = 10 * a + b
					num2 = 100 * c + 10 * d + e
					num3 = num1 * num2
					num3Digits = getDigits(num3)
					l = num3Digits + [a, b, c, d, e]
					l.sort()
					#f.write(str(num1) + " " + str(num2) + " " + str(num3) + " " + str(l) + "\n")

					if l == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
						gl.append((num1, num2, num3))
						if not nl.__contains__(num3):
							nl.append(num3)

					# a * bcde format
					num1 = a
					num2 = 1000 * b + 100 * c + 10 * d + e
					num3 = num1 * num2
					num3Digits = getDigits(num3)
					l = num3Digits + [a, b, c, d, e]
					l.sort()
					#f.write(str(num1) + " " + str(num2) + " " + str(num3) + " " + str(l) + "\n")

					if l == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
						gl.append((num1, num2, num3))
						if not nl.__contains__(num3):
							nl.append(num3)


print gl
print nl
print sum(nl)
