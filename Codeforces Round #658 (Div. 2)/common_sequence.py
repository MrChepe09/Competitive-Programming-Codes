def commonseq(n, a, b):
    for i in range(len(a)):
        if(a[i] in b):
            return a[i]
    return -1

test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = commonseq(n, a, b)
    if(ans==-1):
        print("NO")
    else:
        print("YES")
        print(1, ans)
