def isyana(n, a):
    maxi = -1
    count = 0
    for i in range(n):
        if(a[i]> maxi):
            maxi = a[i]
            if(i==n-1 or a[i]>a[i+1]):
                count+=1
    return count


test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    ans = isyana(n, a)
    print("Case #"+str(i+1)+': '+str(ans))
