 #!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    if(n==0):
        return 0
    set_n = set(ar)
    pairs=0
    for ele in set_n:
        count=0
        for e_list in ar:
            if(ele==e_list):
                count+=1
        pairs+=(count//2)
    return pairs



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
