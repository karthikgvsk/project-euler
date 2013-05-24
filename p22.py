
# Names scores problem

#helper function
def count(s, l):
	i = 0
	sum1 = 0
	while i < l:
		sum1 = sum1 + ord(s[i]) - ord('A') + 1
		i = i + 1
	return sum1



#reading and formatting the string
f = open("names.txt")
s = f.read()
s = s[1:-1]
s = s.split('","')
s.sort()
n = len(s)
i = 0
sum1 = 0
while i < n:
	temp = count(s[i], len(s[i]))
	sum1 = sum1 + (i + 1) * (temp)
	i = i + 1

print sum1
print s[0]
#print count("COLIN", 5)

