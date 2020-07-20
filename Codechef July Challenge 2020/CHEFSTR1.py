def chefstring(n, s):
    res = 0
    for i in range(1, n):
        res += abs(s[i]-s[i-1])-1
    return res

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(chefstring(n, a))
