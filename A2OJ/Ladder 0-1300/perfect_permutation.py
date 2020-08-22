def permutation(n):
    a = []
    if(n%2==1):
        return -1
    for i in range(1, n+1):
        a.append(i)
    for i in range(0, n, 2):
        a[i], a[i+1] = a[i+1], a[i] 

    return a

n = int(input())
ans = permutation(n)
if(ans==-1):
    print(-1)
else:
    print(*permutation(n))