import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    len_str = len(s)
    # double slash gives integer instead of floating in python 3
    num_of_repeated_str = n//len_str
    remainder = n%len_str

    count1 = 0
    count2 = 0

    for i in range(len_str):
        if s[i] == 'a':
            count1 +=1
        if s[i] == 'a' and i < remainder:
            count2 +=1

    total = count1 * num_of_repeated_str + count2   
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
