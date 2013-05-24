global count
count = 0
def findPossibilities(n, l, st, f):
	# base cases
	if n == 0:
		# printing the solutions, which takes the bulk of the time
		f.write(str(st) + " " + str(n) + "\n")
		global count
		count = count + 1
		return
	
	
	# recursion
	if n > 0 and len(l) != 0:
		quo = n // l[-1]
		i = 0
		while i <= quo:
			st.append((i, l[-1]))
			findPossibilities(n - i * l[-1], l[:-1], st, f)
			del st[-1]
			i = i + 1



l = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200
st = []
f = open('myfile','w')
findPossibilities(n, l, st, f)
print count
