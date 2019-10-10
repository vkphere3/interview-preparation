#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count_a = s.count('a')
    if(count_a==0):
        return 0
    extra_chars= n%(len(s))
    total_count= count_a * (n//(len(s)))

    if(extra_chars!=0):
        sub_str= s[0:extra_chars]
        count_a=sub_str.count('a')
        total_count += count_a
    return total_count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
