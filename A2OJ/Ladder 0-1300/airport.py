def airport(n, m, a):
    g = list(a)
    maxi = 0
    for i in range(n):
        amx = max(g)
        maxi += amx
        t = g.index(amx)
        g[t]-=1
    a.sort()
    j = 0
    i = 0
    mini = 0
    while(j<n and i<n):
        if(a[j]!=0):
            mini += a[j]
            a[j]-=1
            i+=1
        else:
            j+=1
    return str(maxi)+" "+str(mini)

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(airport(n, m, a))