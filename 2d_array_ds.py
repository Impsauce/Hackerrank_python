import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.

def _get_hourglass_sum(matrix, row, col):
    sum = 0
    sum += matrix[row-1][col-1]
    sum += matrix[row-1][col]
    sum += matrix[row-1][col+1]
    sum += matrix[row][col]
    sum += matrix[row +1][col-1]
    sum += matrix[row +1][col]
    sum += matrix[row +1][col+1]
    return sum

def hourglassSum(arr):
    #the case of all -9s per our constraints
    max_hourglass_sum = -63
    #can't have a center for an hourglass in first row or last row
    for i in range(1,5):
        #can't have a center for hourglass in first column or last column
        for j in range(1,5):
            current_hourglass_sum = _get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum 
    return max_hourglass_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
