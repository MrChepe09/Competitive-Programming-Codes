def petrbook(n, a):
    total = 0
    i = 0
    while(total<n):
        if(i==7):
            i = 0
        total += a[i]
        i+=1
    return i

n = int(input())
a = list(map(int, input().split()))
print(petrbook(n, a))