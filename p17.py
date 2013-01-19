l = [0, 1, 1]
length = len(l)
while len(str(l[length - 1])) < 1000:
	length = len(l)
	l.append(l[length - 1] + l[length - 2])

length = len(l)
print length - 2

