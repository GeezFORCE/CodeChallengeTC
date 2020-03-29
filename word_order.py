n=int(input())
assert 1<=n<=pow(10,5)
word_list = []
word_order=dict()
leng = 0
for i in range(n):
    word = input()
    assert word.islower()
    leng+= len(word)
    word_list.append(word)
assert n<pow(10,6)
for i in word_list:
    cnt = word_list.count(i)
    if i not in word_order.keys():
        word_order[i]=cnt
print(len(word_order.keys()))
for i in word_order.values():
    print(i,end=" ")


