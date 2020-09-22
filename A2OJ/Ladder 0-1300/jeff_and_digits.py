def cards(n, a):
    f = a.count(5)
    z = a.count(0)
    ans = []
    if(z==0):
        return -1
    g = [5]*((f//9)*9)
    ans+=g
    ze = [0]*z
    if(ans == []):
        return 0
    else:
        ans += ze
        return ''.join(map(str, ans))

n = int(input())
a = list(map(int, input().split()))
print(cards(n, a))