
from math import factorial
def perm(n, s):
        if len(s)==1:
            return s
        q, r = divmod(n, factorial(len(s)-1))
        return s[q] + perm(r, s[:q] + s[q+1:])


print (perm(int(input("Lexicographic permutation of 0123456789? "))-1, '0123456789'))
