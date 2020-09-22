def approach(n, ans):
    global a, ind, b, m
    for i in range(m):
        ans[0] += ind[b[i]]+1
        ans[1] += len(a)-ind[b[i]]
    return ans


n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ind = [0]*(len(a)+1)
for i in range(len(a)):
    ind[a[i]] = i
ans = [0, 0]
#print(ind)
ans = approach(n, ans)
print(*ans)