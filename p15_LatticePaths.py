import timeit
import functools

###################### METHOD 1 : Python Cache Implementation ##########
# @functools.cache
# def get_paths(x,y):
#     routes = {}
#     if (x,y) in routes:
#         return routes[x,y]
#     elif x==0:
#         r = 1
#     elif x>y :
#         r = get_paths(y,x)
#     else:
#         r = get_paths(x-1,y) + get_paths(x,y-1)
#     routes[x,y] = r
#     return r
#
# strt = time.time()
# print(get_paths(20,20))
# print(time.time()-strt)

################# METHOD 2 : Memooize Implementation ####################

# def memoize(func_called):
#     cache = {}
#     def memoized(*args):
#         if args in cache:
#             return cache[args]
#         result = func_called(*args)
#         cache[args] = result
#         return result
#     return memoized
#
# @memoize
# def get_paths(x,y):
#     if x == 0 or y == 0 :
#         r = 1
#     elif x > y:
#         r = get_paths(y,x)
#     else:
#         r =  get_paths(x-1,y) + get_paths(x,y-1)
#     return r
#
# # below points to memoized function that can be called in next line as function with arguments
# # mem_paths = memoize(get_paths)
# print(get_paths(20,20))
# # print(timeit.timeit('mem_paths', globals=globals(), number=1))
#

################ METHOD 3 : ITERATIVE SOLUTION ##########################

def get_paths(x,y):
    path_list = [[1 if i==0 else 0 for i in range(0,y+1) ] if j!= 0 else [1 for _ in range(0,y+1)] for j in range(0,x+1)]
    print(path_list)
    for i in range(1,x+1):
        for j in range(1,y+1):
            path_list[i][j] = path_list[i-1][j]+path_list[i][j-1]
    return path_list[x][y]


print(get_paths(20,20))
print(timeit.timeit('get_paths', globals=globals(), number=1))









