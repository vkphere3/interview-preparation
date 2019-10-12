#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=[]
    for v in range(len(arr)-2):
        for i in range(len(arr)-2):
            sum.append(arr[v][i]+arr[v][i+1]+arr[v][i+2]+arr[v+1][i+1]+arr[v+2][i]+arr[v+2][i+1]+arr[v+2][i+2])
    return max(sum)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
