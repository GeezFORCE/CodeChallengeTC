def minion_game(string):
    vowels = "AEIOU"
    consonants = "QWRTYPSDFGHJKLZXCVBNM"
    players=dict()
    assert len(vowels)+len(consonants)==26
    players["Kevin"]=len(sorted(s[i:j] for i, x in enumerate(s) for j in range(i + 1, len(s) + 1) if x in vowels))
    players["Stuart"]=len(sorted(s[i:j] for i,x in enumerate(s) for j in range(i+1,len(s)+1) if x in consonants))
    max_key=max(players,key=players.get)
    if players["Stuart"]!=players["Kevin"]:
        print(max_key,players[max_key])
    else:
        print("Draw")
s=input()
minion_game(s)  