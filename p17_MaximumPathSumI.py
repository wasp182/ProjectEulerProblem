with open('ProjectEuler_problem18.txt','r') as FILE:
    Data = FILE.readlines()
    print(Data)
    arr = [list(map(int,(j.split()))) for j in Data]

print(arr)
for rk in range(len(arr)):
    if rk > 0:
        for ci in range(len(arr[rk])):
            arr[rk][ci] += max(arr[rk-1][max(ci-1,0)],arr[rk-1][min(ci,rk-1)])

print(max(arr[len(arr)-1]))