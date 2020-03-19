n = int(input())
calorie = list(map(int,input().split()))
pro = 0
assert 1<=len(calorie)<=40
for i in calorie:
    assert 1<=i<=1000
two_list = [2**i for i in range(len(calorie))]
two_list.sort()
calorie.sort()
calorie.reverse()
for i in range(len(calorie)):
    pro = pro + calorie[i]*two_list[i]
print(pro)
