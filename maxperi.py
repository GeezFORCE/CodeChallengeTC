n = int(input())
sticks = list(map(int, input().split()))

assert 3<=len(sticks)<=50
list1=[]
for i in sticks:
    assert 1<=i<=pow(10,9)
sticks.sort()
sticks.reverse()
for i in range(len(sticks)):
    try:
        a,b,c = sticks[i:i+3]
    except:
        print(-1)
        exit()
    if a+b>c and b+c>a and a+c>b:
        list1.append(a)
        list1.append(b)
        list1.append(c)
        list1.sort()
        break
if len(list1)==0:
    print(-1)
else:
    print(list1)