#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the counterGame function below.
def counterGame(n):
    who = sum(i == 1 for i in bin(n-1)[2:])
    if who&1:
        return("Louise")
    else:
        return("Richard")
for t_itr in range(t):
    n = int(input())

result = counterGame(n)
print(result)
