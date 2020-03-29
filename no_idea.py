n,m = list(map(int,input().split()))
n_list = list(map(int,input().split()))
A = set(map(int,input().split()))
B =set(map(int,input().split()))
assert 1<=n<=pow(10,5)
assert 1<=m<=pow(10,5)
for i in n_list:
    assert 1<=i<=pow(10,9)
for i in A:
    assert 1<=i<=pow(10,9)
for i in B:
    assert 1<=i<=pow(10,9) 
happiness=0
for i in n_list:
    if i in A:
        happiness+=1
    elif i in B:
        happiness-=1
    else:
        continue
print(happiness)

