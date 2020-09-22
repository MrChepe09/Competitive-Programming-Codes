def rainbow(n, a):
    if(a != a[::-1]):
        return "no"
    for i in range(1, n):
        if(abs(a[i]-a[i-1])!=1 and a[i]-a[i-1]!=0):
            return "no"
    for i in range(1, 8):
        if(i not in a):
            return "no"
    return "yes"


test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(rainbow(n, a))