import numpy as np

with open('ProjectEuler_problem18.txt','r') as FILE:
    Data = FILE.readlines()
    print(Data)
    arr = [list(map(int,(j.split()))) for j in Data]

print(arr)
arr2 = arr.copy()
for index,row in enumerate(arr):
    print(index)

print("hello")