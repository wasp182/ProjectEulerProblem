def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1)*n

nums = factorial(100)
sum_digit = 0
while nums > 0:
    sum_digit += nums % 10
    nums = nums//10

print(sum_digit)