def coder(n, a):
    mini = a[0]
    maxi = a[0]
    count = 0
    for i in range(1, n):
        if(a[i]>maxi):
            maxi = a[i]
            count += 1
        elif(a[i]<mini):
            mini = a[i]
            count += 1
    return count

n = int(input())
a = list(map(int, input().split()))
print(coder(n, a))