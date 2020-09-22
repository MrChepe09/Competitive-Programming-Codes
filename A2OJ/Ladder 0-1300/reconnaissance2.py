def recon(n, a):
    mini = 9999
    s1 = 1
    s2 = 1
    for i in range(n):
        if abs(a[i]-a[i-1]) < mini:
            mini = abs(a[i]-a[i-1])
            s1 = i+1
            s2 = i
    if(s2==0):
        s2 = n
    return str(s2)+" "+str(s1)


n = int(input())
a = list(map(int, input().split()))
print(recon(n, a))