import string
h = list(map(int, input().rstrip().split()))
for i in h:
    assert 1<= i <=7
word = input()
alphabets = dict(zip(string.ascii_lowercase,h))
word_height=[]
for i in list(word):
    word_height.append(alphabets[i])
max_height=max(word_height)
print(max_height*len(word))

