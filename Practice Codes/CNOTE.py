def notebook(x, y, k, a):
    diff = x-y
    for i in a:
        if(i[0]>=diff and i[1]<=k):
            return "LuckyChef"
    return "UnluckyChef"


test = int(input())
for i in range(test):
    x, y, k, n = map(int, input().split())
    a = []
    for i in range(n):
        p, c = map(int, input().split())
        a.append([p, c])
    print(notebook(x, y, k, a))