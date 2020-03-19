s=input()
s=list(s)
o = []
visited = []
for i in range(len(s)):
    if s[i] not in visited:
        visited.append(s[i])
        count = s.count(s[i])
        print(count)
        if count%2!=0:
            o.append(s[i])
o = "".join(o)
if len(o)!=0:
    print(o)
else:
    print("Empty String")