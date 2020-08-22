def soldier(n, a):
    maxi = max(a)
    mini = min(a)
    for i in range(n):
        if(a[i]==maxi):
            maxind = i
            break
    for i in range(n-1, -1, -1):
        if(a[i]==mini):
            minind = i
            break
    if(maxind>minind):
        return maxind+((n-1)-minind-1)
    else:
        return maxind+((n-1)-minind)

n = int(input())
a = list(map(int, input().split()))
print(soldier(n, a))