def kstring(n, s):
    dicti = {}
    for i in s:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
    for i in dicti:
        if(dicti[i]%n!=0):
            return -1
    res = []
    for i in range(n):
        for j in dicti:
            res.append(j*(dicti[j]//n))
    ans = ''.join(res)
    return ans

n = int(input())
s = input()
print(kstring(n, s))