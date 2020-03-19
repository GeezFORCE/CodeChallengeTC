n,k=list(map(int,input.split()))
contests = []
for _ in range(n):
    contests.append(list(map(int,input.split())))
assert 1<=n<=100
assert 0<=k<=n
for i in contests:
    assert 1<=i[0]<=pow(10,4)
    assert i[1]==0 or i[1]==1
