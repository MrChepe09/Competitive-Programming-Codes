def drinks(n, a):
    return (sum(a))/(n)

n = int(input())
a = list(map(int, input().split()))
print(drinks(n, a))