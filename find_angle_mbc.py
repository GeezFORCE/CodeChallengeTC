import math
ab = int(input())
bc = int(input())
assert 0<=ab<=100 and 0<=bc<=100
print(math.asin((abs(complex(bc,ab))/2))/bc)