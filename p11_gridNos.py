import time
from math import prod

data = []
with open("grid_data.txt",'r',encoding="utf-8") as inpstream:
    for lines in inpstream.readlines():
        columns = []
        for items in lines.split(" "):
            columns.append(int(items))
        data.append(columns)
print(data)

strt_time = time.time()

# data loaded in 2 D array
n = len(data)
m = len(data[0])

def brute_prod():
    strt_time = time.time()
    sum_list = [[0]*m]*n
    highest_sum = 0
    left_diagonal_sum,right_diagonal_sum,right_sum,down_sum = 0,0,0,0
    for i in range(n-3):
        for j in range(m-3):
            if j <= m-4:
                right_sum = prod(data[i][k] for k in range(j,j+4))
            if i <= m-4:
                down_sum = prod(data[k][j] for k in range(i,i+4))
            if i <= n-4 and j <= m-4:
                right_diagonal_sum = prod(data[i+temp][j+temp] for temp in range(0,4))
            if i <= n-4 and j >= 3:
                left_diagonal_sum = prod(data[i+temp][j-temp] for temp in range(0,4))
            current_sum = max(left_diagonal_sum,right_diagonal_sum,right_sum,down_sum)
            sum_list[i][j] = current_sum
            if current_sum > highest_sum:
                highest_sum = current_sum

    print(sum_list)
    print(highest_sum,time.time()-strt_time)

def prod_optimize():
    strt_time = time.time()
    sum_list = [[0]*m]*n
    highest_sum = 0
    left_diagonal_sum,right_diagonal_sum,right_sum,down_sum = 0,0,0,0
    for i in range(n-3):
            for j in range(m-3):
                right_sum = prod(data[i][k] for k in range(j,j+4))
                down_sum = prod(data[k][j] for k in range(i,i+4))
                right_diagonal_sum = prod(data[i+temp][j+temp] for temp in range(0,4))
                left_diagonal_sum = prod(data[i+temp][j-temp] for temp in range(0,4) if j>=3 )
                current_sum = max(left_diagonal_sum,right_diagonal_sum,right_sum,down_sum)
                sum_list[i][j] = current_sum
                if current_sum > highest_sum:
                    highest_sum = current_sum
    print(sum_list)
    print(highest_sum,time.time()-strt_time)

brute_prod()
prod_optimize()