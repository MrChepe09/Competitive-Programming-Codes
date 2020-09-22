def flowers(n, a):
    a.sort()
    maxdiff = a[-1]-a[0]
    if(sum(a)==n*a[0]):
        return [maxdiff, (n*(n-1)//2)]
    
    c1 = a.count(a[0])
    c2 = a.count(a[-1])
    return [maxdiff, c1*c2]


n = int(input())
a = list(map(int, input().split()))
print(*flowers(n, a))