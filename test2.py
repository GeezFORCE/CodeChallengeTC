text = input()
text = text.lower()
words = text.split()
for word in words:
    keys = ["https://","http://","www."]
    addr = [i for i in word.split(".")]
    if any(item in addr for item in keys):
        print(word)
