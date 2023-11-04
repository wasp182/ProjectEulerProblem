import math

from p27_QuadraticPrimes import prime_list

#2 Returns max powers of divisor
def power_factor(num, num2):
    # we only consider powers if  num2 divides num
    if num % num2 != 0 :
        return 0
    pwr = 1
    num = num / num2
    while num > 0:
        if num % num2 == 0:
            pwr += 1
        num = num / num2
    return pwr
print(power_factor(625,20))


def prime_factorization(k):
    #1 get a list of primes that divide k
    list_primes = prime_list(k)
    initial_prime_factors = []
    prime_powers = []
    #1.1 generate list of primes that divide k - prime factors
    for p in list_primes:
        if k % p == 0:
            initial_prime_factors.append(p)
    #2 Get powers of prime factors
    for p1 in initial_prime_factors:
        max_power = power_factor(k,p1)
        prime_powers.append(max_power)
    return initial_prime_factors , prime_powers
print(prime_factorization(95))

a = 100
b = 100
prime_a = prime_list(a)
non_prime_a = [x for x in range(2, a+1) if x not in prime_a]

print(len(prime_a))
print(non_prime_a)

collision = 0
for a_p in non_prime_a:
    max_non_prime = max(non_prime_a)
    # number of prime factors > 1 or not
    num_pf = 0
    pf = 0
    for k in prime_a:
        if a_p % k == 0:
            num_pf += 1
            # store the prime that divides it , in case num_pf = 1
            # use that to get (m) st p**m = a
            pf = k
        if num_pf > 1:
            break

    if num_pf == 1:
        m = power_factor(a_p,pf)
        # check for powers less than m that can divide m*i: i belongs to {1,b}
        if m > 2:
            for i in range(m*2,b*m+1,m):
                for x in range(2,m):
                    if i % x == 0 :
                        collision += 1
                        break
        if m == 2:
            collision += (b//m - 1)
        print(a_p,collision)

print()
print(collision)
uniques = (a-1)**2 - collision
print(uniques)