s = input()
print sum(s[i] != "SOS"[i%3] for i in range(len(s)))

    count = 0
    assert 1<=len(s)<=99
    if len(s)%3 == 0 and s.isalpha() == True and s.isupper() == True:
        s = list(s)
        for i in range(0,len(s),3):
            if "".join(s[i:i+3])!="SOS":
                count = count+1
        print(count)
    else:
        exit()