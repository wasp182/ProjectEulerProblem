def sum_of_digits():
    no = 2**1000
    sum_digits = 0
    while no > 0 :
        sum_digits +=  no % 10
        no = no//10
    return sum_digits

if __name__ == "__main__":
    print(sum_of_digits())

