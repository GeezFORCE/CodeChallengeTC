import math
n = int(input())
assert 1<=n<=pow(10,16)
num=5
count = 0
while True:
    fact = list(str(math.factorial(num)))
    fact.reverse()
    for i in fact:
        if i == "0":
            count+=1
        if i!= "0":
            break
    if count == n:
        print(num)
        break
    else:
        count = 0
        num+=1
                