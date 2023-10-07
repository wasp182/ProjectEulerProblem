# How many Sundays fell on the first of the month during the twentieth
# century (1 Jan 1901 to 31 Dec 2000)?

import datetime as dt
import timeit
import pprint

# Approach 1 : Brute Force
# Loop over years , days , months

print("###First Approach###","\n")
t1=timeit.timeit()
nums = 0
for i in range(1901,2001):
    for j in range(1,13):
        if dt.datetime(i,j,1).weekday() == 6 :
            nums += 1
t2=timeit.timeit()
print(t2-t1)
print(nums,"\n")

# Approach 2 : use only one loop to iterate over years
# without weekday function
# 1 Jan 1990 was Monday

# Generate dictionary of days per month
dicts = {i: 31 if i not in (4, 6, 9, 11) else 30 for i in range(1,13)}
# print(dicts)

print("###Second Approach###","\n")

t1=timeit.timeit()
num2 = 0
sunday_code = 0
for yr in range(1900,2001):
    for mon in range(1,13):
        sunday_code = (sunday_code+int(dicts[mon])) % 7
        if yr == 1900:
            break
        if sunday_code == 0:
            num2 += 1
t2=timeit.timeit()
print(t2-t1)
print(num2)