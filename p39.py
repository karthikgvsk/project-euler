# Integer right triangles
from math import sqrt, floor

p_max = 1000
n1 = p_max // 2 
n2 = p_max // 3
mainList = [None] * (p_max + 1)
b = 1
count = 0
while b <= n1 + 1:
	a = 1
	while a <= min(b, n2 + 1):
		c = sqrt(a**2 + b**2)
		if floor(c) == c:
			p = a + b + int(c)
			if p <= p_max:
				if mainList[p] == None:
					mainList[p] = [(a, b, int(c), p)]
				else:
					mainList[p].append((a, b, int(c), p))
		a = a + 1
	b = b + 1

print "---"
m = 0
index = 0
for i in range(p_max + 1):
	if mainList[i] != None and m < len(mainList[i]):
		m = len(mainList[i])
		index = i
	#print i, mainList[i]

print "---"
print m
print index, mainList[index]
print mainList[120]
