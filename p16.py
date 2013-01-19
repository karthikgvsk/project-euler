#lattice paths problem
#the answer is 2nCn (combinatorics)
n = 3
num1 = 1
num2 = 1
for i in range(n + 1, 2 * n + 1):
	num1 = num1 * i
	num2 = num2 * (i - n)
print num1 / num2
