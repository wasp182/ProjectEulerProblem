import timeit


def repeated_decimal(n : int):
    digit_list = []
    remainder_list = []
    numerator = 10
    while True:
        while numerator < n:
            numerator *= 10
            digit_list.append(0)
        remainder = numerator % n
        quotient = numerator // n
## when remainder starts repeating then we have arrived at end of reciprocal cycle
        if remainder not in remainder_list and remainder != 0:
            digit_list.append(quotient)
            remainder_list.append(remainder)
            # print(f"digits : {digit_list}")
            # print(remainder_list)
            numerator = remainder*10
        else:
            digit_list.append(quotient)
            # print(f"break {quotient} , {remainder}")
            break
# remainder list is the one that should be used to judge length of reciprocal cycle
    return len(remainder_list)

#Test - with 7 , 44 , 14
# print(repeated_decimal(7))

t1 = timeit.timeit()
list_decimals = []
for i in range(2,1000):
    x = repeated_decimal(i)
    list_decimals.append(x)

t2 = timeit.timeit()

most_cyles = max(list_decimals)
# add 2 casue our list starts with 2 and not 0
num_most_cycles = list_decimals.index(most_cyles) + 2
print(f"Largest reciprocal cycle {num_most_cycles} with {most_cyles} cycles")
print(t1-t2)





