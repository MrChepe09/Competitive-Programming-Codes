from sys import stdin, stdout
s = stdin.readline().strip('\n')
s += '$'
n = len(s)
c = [0 for _ in range(n)]
p = [0 for _ in range(n)]
a = []
for i in range(n):
    a.append([s[i], i])
a.sort()
for i in range(n):
    p[i] = a[i][1]
#print(a, p)
c[p[0]] = 0
for i in range(1, n):
    if(a[i][0] == a[i-1][0]):
        c[p[i]] = c[p[i-1]]
    else:
        c[p[i]] = 1 + c[p[i-1]]
 
k = 0
while((1 << k) < n):
    a = [0 for _ in range(n)]
    for i in range(n):
        a[i] = [[c[i], c[(i + (1<<k)) % n]], i]
    a.sort()
    for i in range(n):
        p[i] = a[i][1]
    c[p[0]] = 0
    for i in range(1, n):
        if(a[i][0] == a[i-1][0]):
            c[p[i]] = c[p[i-1]]
        else:
            c[p[i]] = 1 + c[p[i-1]]
    k+=1
 
for i in range(n):
    stdout.write(str(p[i])+" ")