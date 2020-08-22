def check(s):
    z = s[0]
    for i in s:
        if(i!=z):
            break
    if(i>z):
        return 1
    else:
        return 0

def kmp(s, sub):
    s = list(s)
    sub = list(sub)
    s.sort()
    dicti = {}
    new = []
    for i in s:
        if(i in dicti):
            dicti[i] += 1
        else:
            dicti[i] = 1
    for i in sub:
        dicti[i] -= 1
    mini = sub[0]
    for i in dicti:
        if(i==mini):
            if(check(sub)):
                new.append(i*dicti[i])
                new += sub
            else:
                new += sub
                new.append(i*dicti[i])
        else:
            new.append((i)*dicti[i])
    return ''.join(new)

test = int(input())
for i in range(test):
    s = input()
    sub = input()
    print(kmp(s, sub))
