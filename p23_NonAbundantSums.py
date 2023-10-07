import math


def divisor(i):
    divisor_list = set()
    divisor_list.add(1)
    for j in range(2,int(math.sqrt(i)+1)):
        if i % j == 0 and j not in divisor_list:
            divisor_list.add(j)
            divisor_list.add(i//j)
    return sum(divisor_list)


# upper limit given in question
abundant_list = []
for k in range(1,28124):
    if divisor(k) > k :
        abundant_list.append(k)
print("List of abundant nos till 28123")
print(abundant_list)

sum_set=set()
for index,first in enumerate(abundant_list):
    for second in abundant_list[index:]:
        if first+second <= 28123:
            sum_set.add(first+second)

print()
print("Integers that can't be represented as sum of 2 non abundant integers")
print(set([_ for _ in range(1,28123)]) - sum_set)
print(sum(set([_ for _ in range(1,28123)]) - sum_set))
