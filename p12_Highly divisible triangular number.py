from math import sqrt , log
import time
# from prime import is_prime_sieve

def no_of_divisors_brute(n):
    nod = 1
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            nod += 2
        if i*i == n :
            nod -=1
    return nod


def factors(n):
    factors = []
    for index in range(1,int(sqrt(n))+1):
        if n % index == 0:
            factors.append(index)
    return factors

def is_perfect_square(n):
    s1 = int(sqrt(n))
    return s1*s1 == n

def is_triangular(n):
    return is_perfect_square(1+8*n)

def is_prime(n):
    for index in range(2,int(sqrt(n))+1):
        if n % index == 0:
            return False
    return True

def primes_sieve_method(n):
    primes = [True for _ in range(0,n+1)]
    primes[0] = False
    primes[1] = False
    p=2
    while p*p < n :
        if primes[p] == True:
            for nos in range(p*2,n+1,p):
                primes[nos] = False
        p+=1
    return primes

def print_factors(n):
    for index in range(1,n+1):
        print(len(factors(index)))

def primes(n):
    primes = []
    index = 2
    while index*index < n :
        if is_prime(index) and n % index == 0:
            primes.append(index)
        index += 1
    return primes

def max_power(n,p):
    power = 0
    while n % p == 0 :
        n = n//p
        power += 1
    return power


# returns no of divisors in increasing order till n
def check_divisors(n):
    temp = 2
    temp_index=1
    # primes_list = primes_sieve_method(n)
    for index in range(2,n):
        factor_list = factors(index)
        # prime_factors=[]
        if len(factor_list) > temp:
                temp = len(factor_list)
                temp_index = index
    return temp_index,temp


# returns list of prime factors and their power
def prime_factors(n):
    primes_list = primes_sieve_method(n)
    factor_list = factors(n)
    prime_factors=[]
    prime_powers=[]
    for items in factor_list:
        if primes_list[items] == True:
            prime_factors.append(items)
            prime_powers.append(max_power(n,items))
    return prime_factors , prime_powers

def prime_factors_optimal(n):
    primes_list = primes_sieve_method(n)
    prime_factors=[]
    prime_powers=[]
    for items in primes_list:
        if n % items == 0 :
            prime_factors.append(items)
            prime_powers.append(max_power(n,items))
    return prime_factors,prime_powers

def prime_factors_optimal(n,primes_list):
    prime_factors=[]
    prime_powers=[]
    for items in primes_list:
        if n % items == 0 :
            prime_factors.append(items)
            prime_powers.append(max_power(n,items))
    return prime_factors,prime_powers

def prime_factors_nod(n,prime_list):
    nod = 1
    for items in prime_list:
        if n % items == 0:
           exp = max_power(n,items)
           nod *= exp + 1
    return nod


def factor_count(limit,primes_list):
    cnt , i = 0 , 1
    Dn , Dn1 = 2,2
    while cnt < limit :
        if i % 2 == 0 :
            Dn = prime_factors_nod(i+1,primes_list)
            cnt = Dn*Dn1
        else:
            Dn1 = prime_factors_nod((i+1)/2,primes_list)
            cnt = Dn*Dn1
        i += 1
    return cnt , i*(i-1)/2


if __name__ == "__main__":
    # no_of_divisors , i = 1 ,45360
    # while no_of_divisors < 100:
    #     index , temp = check_divisors(i)
    #     if temp > no_of_divisors:
    #         print(f" {i} : # Minimum Divisor : {index}, No of factors : {temp}")
    #         no_of_divisors = temp
    #     i+=1
    # max_divisor , max_index= 1,1
    ################## USING PRIME FACTORISATION METHOD #################
    # while no_of_divisors < 500 :
    #     if i % 12 == 0 and is_triangular(i) :
    #         no_of_divisors = 1
    #         # get prime factor list and its corresponding power
    #         f,p = prime_factors(i)
    #         # print(f" prime factors of {i} : {f} , {p}")
    #         for items in p:
    #             no_of_divisors *= (1+items)
    #         if no_of_divisors > max_divisor:
    #             max_divisor = no_of_divisors
    #             max_index = i
    #             print(f" {max_index} : {max_divisor}")
    #         i += 1
        # print(f" {i} : {no_of_divisors}")

################## BRUTE FORCE #######################################
    # strt_time = time.time()
    # n = 0
    # i = 1
    # print(no_of_divisors_brute(4))
    # while  no_of_divisors_brute(n) < 500 :
    #     n += i
    #     i += 1
    # print(n)
    # delta = time.time() - strt_time
    # print(f"time : {delta}")

################# OPTIMAL METHOD #####################################
    strt_time2 = time.time()
    prime_list = [index for index,items in enumerate(primes_sieve_method(75000)) if items == True ]
    print(factor_count(500,prime_list))
    delta = time.time() - strt_time2
    print(f"time : {delta}")