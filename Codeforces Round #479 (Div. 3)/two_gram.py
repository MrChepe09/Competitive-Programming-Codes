def problemB(n, s):
    dicti = {}
    for i in range(n):
        sub = s[i:i+2] 
        if(sub in dicti):
            dicti[sub]+=1
        else:
            dicti[sub] = 1
    return max(dicti, key=dicti.get)


n = int(input())
s = input()
print(problemB(n, s))
