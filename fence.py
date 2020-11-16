def fence(a, b, c):
    return (a+b+c)-1

n = int(input())
for i in range(n):
    a, b, c = map(int, input().split())
    print(fence(a, b, c))
