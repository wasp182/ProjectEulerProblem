# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#     a2 + b2 = c2
#
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math

def triplets(N):
    No = int(math.sqrt(N))
    print(No)
    for m in range(2,No):
        for n in range(1,No):
            if m>n:
                a = m**2 - n**2
                b = 2*m*n
                c = m**2 + n**2
            if a+b+c == N:
                print(a*b*c)
                return (a,b,c)


print(triplets(1000))

