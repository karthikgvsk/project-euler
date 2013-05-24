# Counting Sundays Problem

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 1st jan 1901 is tuesday
init = 2
year = 1901
sum1 = 0
temp = init
while year < 2001:
	if year % 4 == 0:
		months[1] = 29
	else:
		months[1] = 28
	
	for i in months:
		if temp % 7 == 0:
			sum1 = sum1 + 1
			print year
		temp = (temp + i) % 7
	temp = temp % 7
	year = year + 1
print sum1
