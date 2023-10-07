# https://projecteuler.net/overview=0021
import math
import timeit

######## APPROACH 1 ########################################

def divisor(i):
    divisor_list = [1]
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0 and j not in divisor_list:
            divisor_list.append(j)
            divisor_list.append(i//j)
    return sum(divisor_list)

t1 = timeit.timeit()
checked_nos = []
nums = 0
store = []
for i in range(1,10001):
    if i not in checked_nos:
        s1 = divisor(i)
        s2 = divisor(s1)
        if i == s2 and i != s1:
            nums += 2
            store.extend((i,s1))
        checked_nos.extend((i,s1))

t2 = timeit.timeit()
print(t1-t2)
print(f"Number of amicable number {nums}")
print(store)
print(sum(store))


