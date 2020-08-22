def word(s):
    lower = 0
    upper = 0
    for i in s:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    if(upper>lower):
        return s.upper()
    else:
        return s.lower()

s = input()
print(word(s))