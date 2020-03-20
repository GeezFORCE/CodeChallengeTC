#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    assert 1<=n<=pow(10,5)
    count_list = []
    for i in range(n):
        count_list.append(min(abs(i-c[j]) for j in range(len(c))))
    return(max(count_list))
nm = input().split()
n = int(nm[0])
m = int(nm[1])
assert 1<=m<=n
c = list(map(int, input().rstrip().split()))
result = flatlandSpaceStations(n, c)
print(result)
