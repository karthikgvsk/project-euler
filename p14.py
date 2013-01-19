def collatz(n):
	i = 1
	d = {}
	d[1] = 1
	max1 = 0
	maxNum = 0
	while  i < n:
		count = 0
		j = i
		while(not d.has_key(j)):
			if(j % 2) == 0:
				j = j / 2
			else:
				j = 3 * j + 1
			count = count + 1
		d[i] = count + d[j]
	
		if max1 < d[i]:
			max1 = d[i]
			maxNum = i
		i = i + 1

	return maxNum

n = 1000000
print collatz(n)
		
