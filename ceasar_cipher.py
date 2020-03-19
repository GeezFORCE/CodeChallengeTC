import string
n=int(input())
s=input()
k=int(input())
assert 1<=len(s)<=100
assert 1<=k<=100
s=list(s)
new_s = ""
alphabets = dict(zip(string.ascii_lowercase,range(1,27)))
key_list = list(alphabets.keys())
value_list = list(alphabets.values())
for i in s:
    if i.lower() in key_list:
        al_index = alphabets.get(i.lower())
        new_al = key_list[value_list.index((al_index+k)%26)]
        if i.isupper():
            new_al = new_al.upper()
        new_s = new_s + new_al
    elif i == "-":
        new_s = new_s + "-"
print(new_s)