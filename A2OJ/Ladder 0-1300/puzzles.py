def puzzle(n, m, a):
    a.sort()
    mini = float('inf')
    for i in range(m-n+1):
        if(a[i+n-1]-a[i]<mini):
            mini = a[i+n-1]-a[i]
    return mini

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(puzzle(n, m, a))