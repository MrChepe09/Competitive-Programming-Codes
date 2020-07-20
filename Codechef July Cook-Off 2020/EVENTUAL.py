def eventual(n, s):
    dicti = {}
    for i in s:
        if(i in dicti):
            dicti[i] += 1
        else:
            dicti[i] = 1
    for i in s:
        if(dicti[i]%2==1):
            return "NO"
    return "YES"

test = int(input())
for i in range(test):
    n = int(input())
    s = input()
    print(eventual(n, s))
