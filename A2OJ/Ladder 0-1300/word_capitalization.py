def capital(s):
    s = list(s)
    if(s[0].islower()):
        s[0] = s[0].upper()
    return ''.join(s)

s = input()
print(capital(s))