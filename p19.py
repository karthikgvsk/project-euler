# no of letters used from 1 to 1000 problem
# counting numbr of types of words used and then ....
# one trivial thing, counting no of "and"s
sum1 = (99 * 9) * (3)

sum5 = (100 * 9) * (7)
#number of hunders digit letters and units digit letters
sum2 = (10 * 9 + 100) * (3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4)

sum3 = (10) * (3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8)

sum4 = (10 * 10) * (6 + 6 + 6 + 5 + 5 + 7 + 6 + 6)

print sum1 + sum2 + sum3 + sum4 + sum5
