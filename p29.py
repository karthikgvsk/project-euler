# Problem 29 :  Distinct powers
# brute force
l = []
a = 2
while a <= 100:
	b = 2
	while b <= 100:
		num = a ** b
		if not l.__contains__(num):
			l.append(num)
		b = b + 1
	a = a + 1
print len(l)
