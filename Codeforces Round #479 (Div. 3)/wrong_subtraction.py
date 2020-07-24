def problemA(n, a):
    for i in range(k):
        if(str(n)[-1]=='0'):
            n = int(n/10)
        else:
            n = n - 1
    return n


n, k = map(int, input().split())
print(problemA(n, k))
