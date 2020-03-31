company_name=list(input())
assert 3<len(company_name)<pow(10,4)
logo=dict()
company_name.sort()
letter_count=0
for letter in company_name:
    letter_count=0
    if letter not in logo:
        letter_count+=1
        logo[letter]=letter_count
    else:
        logo[letter]+=1
letter_count=0
for letter in sorted(logo, key=logo.get, reverse=True):#reverse=true for getting values from behind
    if letter_count<3:
        print(letter,logo[letter])
        letter_count+=1