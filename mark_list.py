n = int(input())
assert 0<n<=100
for i in range(n):
    inp_list=list(map(str,input().split())) 

ind=-1
for i in data_list:
    if i=="MARKS":
        ind = data_list.index(i)
    elif (data_list.index(i)+n)%5==0 and ind!=-1:
        mark_list.append(i)
print(mark_list)        