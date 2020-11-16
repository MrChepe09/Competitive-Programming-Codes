def matrix(n, m, t):
    if(m%2==1):
        return "NO"
    if t == True:
        return "YES"
    else:
        return "NO"

test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    t = 0
    for j in range(n):
        al = list(map(int, input().split()))
        gl = list(map(int, input().split()))
        if al[1] == gl[0]:
            t = True
    print(matrix(n, m, t))