

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
import math


def isPrime(N) -> bool :
    n = int(math.sqrt(N))
    for index in range(2,n+1):
        if N % index == 0:
            return False
    return True

def sum_prime(N):
    sums = 0
    for i in range(2,N+1):
        if isPrime(i):
            sums += i
    return sums

print(sum_prime(2000000))