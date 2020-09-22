def dima(n, f):
    fingers = sum(f)
    c = 0
    for i in range(1, 6):
        if (fingers+i)%(n+1)!=1:
            c+=1
    return c

n = int(input())
f = list(map(int, input().split()))
print(dima(n, f))