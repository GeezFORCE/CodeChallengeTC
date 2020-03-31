def eval(n,sides):
    assert 1<=n<=pow(10,5)
    for i in sides:
        assert 1<=i<=pow(2,31)
    i=0
    while i<n-1 and sides[i]>=sides[i+1]:
        i+=1
    while i<n-1 and sides[i]<=sides[i+1]:
        i+=1
    if i==n-1:
        return True
    else:
        return False
t=int(input())
assert 1<=t<=5
op_list=[]
for i in range(t):
    n=int(input())
    sides=list(map(int,input().split()))
    boole=eval(n,sides)
    if boole:
        op_list.append("Yes")
    else:
        op_list.append("No")
for i in op_list:
    print(i)