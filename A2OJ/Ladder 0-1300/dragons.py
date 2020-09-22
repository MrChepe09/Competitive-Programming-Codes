def dragon(s, n, a):
    a.sort()
    for i in a:
        if(i[0]>=s):
            return "NO"
        else:
            s+=i[1]
    return "YES"


s, n = map(int, input().split())
a = []
for i in range(n):
    x, y = map(int, input().split())
    a.append([x, y])
print(dragon(s, n, a))