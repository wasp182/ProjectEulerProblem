# # declare function sum
# def sum(dim):
#     n = (dim - 1) /2;#find n
#     # use the formula defined above
#     x = (3 + 2 * n * ( 8 * n * n + 15 * n +13)) /3
#     return x
#
# def main():
#     # call the function and print the value
#     diagonal = sum(1001)
#     print (diagonal)
# main()

# Second approach to fill a numpy array and populate it
import numpy as np

n = 11
ptr = n*n
pivot = "left"
z = np.zeros((n,n))
row , col = 0, n-1
z[0,n-1] = ptr
z[n//2,n//2] = 1

while ptr > 2:
    ptr = ptr - 1
    # in first quadrant , pivot changes below diagonal element
    match pivot:
        case "left":
            col -= 1
        case "down":
            row += 1
        case "right":
            col += 1
        case "up":
            row -= 1
    z[row,col] = ptr

    # change in pivot basis their position near diagonal
    # row + col == n is for top right quadrant
    # once you are near diagonal - check quadrant of matrix and change direction
    if row + col == n or row + col == n-1 or row == col:
        if (row + col == n) and row < n/2 and col > n/2 :
            pivot = "left"
        elif row < n/2 and col < n/2:
            pivot = "down"
        elif row > n/2 and col < n/2:
            pivot = "right"
        elif row > n/2 and col > n/2:
            pivot = "up"

print(z)