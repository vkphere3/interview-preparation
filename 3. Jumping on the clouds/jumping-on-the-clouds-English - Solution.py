#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps=0
    n = len(c)
    i=0
    while(i<n-2):
        if(c[i+2]==0):
            steps+=1
            i+=2
        else:
            steps+=1
            i+=1
    if(n-i == 2):
        steps+=1
    return steps


        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
