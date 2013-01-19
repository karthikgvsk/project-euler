#what is the 10001st prime?

from math import log
n = 10001
#using pi(x) limit(a number theory thm), we get pi(x) value as
#pi(x) <= x / ln(x) and here pi(x) = 10001
# and sieve of eratosthenes is used here
val = 100 * n
l = [0] * (val + 2)
l[0] = 1
l[1] = 1

i = 2
while i <= val:
	j = 2
	while j <= val / i:
		if i * j <= val:
			l[i * j] = 1
		j = j + 1
	i = i + 1

i = 0
count = 0
reqd = 0
while i <= val:
	if l[i] == 0:
		count = count + 1
		if count == 10001:
			print i
			break
	i = i + 1

print reqd
