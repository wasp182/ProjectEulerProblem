import timeit


# Create Quadratic function that can generate primes
def prime_function(a,b,prime_list):
    n = 0
    # iterate over n  to see if prime or not , Max n -> b
    if b == 0 or b not in prime_list:
        return n
    while n < abs(b):
        p = n**2 + n*a + b
        if p in prime_list:
            n += 1
        else:
            break
    return n


# Generate list of primes below no k
def prime_list(k):
    prime_list = [True for _ in range(k+1)]
    prime_list[0] = False
    prime_list[1] = False
    p = 2
    while p*p <= k:
        if prime_list[p]:
            for i in range(p*p,k+1,p):
                prime_list[i] = False
        p += 1
    return [index for index, i in enumerate(prime_list) if i is True]


if __name__ == "__main__":
    # Create Prime list basis max value b**2 order
    prime_list_b = prime_list(1000*1000)
    print("Test Case")
    print(prime_function(-61, 971,prime_list_b))
    sample_list = []
    max_len = 0
    an ,bn = 0,0

    # Run prime generator
    t1 = timeit.timeit()
    for b in range(1,1001,2):
        for a in range(max(-999,-b),b,2):
            if abs(b) % abs(a) != 0 or a == 1 :
                xn = prime_function(a,b,prime_list_b)
                # print(xn)
                if xn > max_len:
                    max_len = xn
                    an, bn = a, b
        if b == 501:
            print("501 MILE")
            print(an,bn)

    t2 = timeit.timeit()
    print(t1-t2)
    print(max_len,(an,bn))