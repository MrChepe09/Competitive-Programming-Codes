test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    l = list(input().split())
    ans = []
    token = []
    for i in range(k):
        a = list(input().split())
        token += a
    for i in l:
        if(i in token):
            ans.append("YES")
        else:
            ans.append("NO")
    print(*ans)
