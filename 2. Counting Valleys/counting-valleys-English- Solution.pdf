#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    below_sea=0
    count_valley=0
    steps=0
    for step in s:
        if(step=='D'):
            steps-=1
        elif(step=='U'):
            steps+=1
        else:
            steps+=0
        if(steps<0):
            below_sea=-1
        if(steps>=0 and below_sea<0):
            count_valley+=1
            below_sea=0
    return count_valley



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
