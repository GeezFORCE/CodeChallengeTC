import math
#t = int(input())
n = int(input())
i=1
while True:
    fact = list(str(math.factorial(i)))
    if fact.count("0") == n:
        print(i)
        break
    i+=1
