import math


def is_prime_sieve(n):
    sieve = int(math.sqrt(n))
    if n > 2 and (n%2 !=0):
        for i in range(3,sieve):
            if n % i == 0 :
                return False
        return True
    elif n == 2:
        return True
    else:
        return False


print(is_prime_sieve(2))