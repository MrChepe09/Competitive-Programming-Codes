def problemC(n, k, a):
    if(k==n):
        return max(a)
    a.sort()
    if(k==0):
        if(a[0]==1):
            return -1
        elif(a[0]>1):
            return 1
    if(k<=n-1):
        if(a[k]==a[k-1]):
            return -1
        else:
            return a[k-1]

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(problemC(n, k, a))
