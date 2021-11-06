from bisect import bisect_left
def problem3(n, a, x, y, s):
    find = bisect_left(a, x)
    if(find==n):
        find-=1
    if(a[find] > x and find != 0):
        if(abs(a[find]-x) > abs(x-a[find-1])):
            find -= 1
    ans = 0
    if(a[find] < x):
        ans += (x-a[find])
    if(s-a[find] < y):
        ans += (y-(s-a[find]))
    return ans
        

n = int(input())
a = list(map(int, input().split()))
a.sort()
sumi = sum(a)
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    print(problem3(n, a, x, y, sumi))
    
