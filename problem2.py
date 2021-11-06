def problem2(a, b, c, m):
    if(m==0):
        if(max(a, b, c)-(a+b+c-max(a, b, c))<=1):
            return "YES"
        else:
            return "NO"
    else:
        if(max(a, b, c)-(a+b+c-max(a, b, c)) == m+1):
            return "YES"
        return "NO"

test = int(input())
for i in range(test):
    a, b, c, m = map(int, input().split())
    print(problem2(a, b, c, m))
