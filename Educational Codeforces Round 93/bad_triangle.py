def bad_triangle(n, a):
    if(len(a)<3):
        return -1
    if(a[-1]<a[0]+a[1]):
        return -1
    else:
        return [1, 2, n]

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    ans = bad_triangle(n, a)
    if(ans==-1):
        print(-1)
    else:
        print(*ans)
