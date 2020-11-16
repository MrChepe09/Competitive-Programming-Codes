def adadish(n, a):
    al, bl = 0, 0
    a.sort()
    for i in range(len(a)-1, -1, -1):
        if al<=bl:
            al+=a[i]
        else:
            bl += a[i]
    return max(al, bl)


test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(adadish(n, a))
