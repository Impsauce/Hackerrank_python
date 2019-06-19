import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    cloud_number = 0
    while cloud_number < n -1:
        if cloud_number +2 >= n or c[cloud_number+2] ==1:
            cloud_number +=1
            jumps +=1
        else:
            cloud_number +=2
            jumps +=1
    return jumps
           
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
