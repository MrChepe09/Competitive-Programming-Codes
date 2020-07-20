def drdoof(n, a):
    res = 1
    for i in a:
        res *= i
    if(res%2==1):
        return "YES"
    return "NO"


test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(drdoof(n, a))
