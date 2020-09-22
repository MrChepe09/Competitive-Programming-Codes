def polyrel(n):
    ans = n
    while(n//2>2):
        n = n//2
        ans += n
    return ans

test = int(input())
for i in range(test):
    n = int(input())
    for i in range(n):
        a, b = map(int, input().split())
    print(polyrel(n))
