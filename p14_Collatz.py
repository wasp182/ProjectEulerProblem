import time

def collatz_func(n):
    if n % 2 == 0 :
        n = int(n/2)
    else:
        n = 3*n + 1
    return n

def collatz_chain(n):
    chain_len_list = [0 for _ in range(0,n+1)]
    chain_len_list[1]=1
    if n % 2 == 0 :
        chain_len_list[n] = 1 + collatz_chain(n//2)
    else:
        chain_len_list[n] = 2 + collatz_chain((3*n+1)//2)
    return chain_len_list[n]

def test_collatz2(limit):
    max_count = 1
    for i in range(limit//2,limit + 1):
        count = collatz_chain(i)
        if count > max_count:
            max_count = count
            max_index = i
    return max_index,max_count

def collatz_chain(n):
    count = 0
    while n != 1 :
        n = collatz_func(n)
        count += 1
    return count

strt = time.time()
print(test_collatz2(1000000))
print(time.time() - strt)