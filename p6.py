#finding the largest palindrome number which is a product of two 3-digit numbers
def palindrome(n):
	s1 = str(n)
	#if s1 is equal to its reverse, return True
	if s1 == s1[::-1]:
		return True
	else:
		return False

start = 999
end = 100
max = 0
m = start
while m >= end:
	n = start
	while n >= m:
		prod = m * n
		if max >= prod:
			break
		if palindrome(m * n):
			max = m * n
		
		n = n - 1
	m = m - 1

print max

