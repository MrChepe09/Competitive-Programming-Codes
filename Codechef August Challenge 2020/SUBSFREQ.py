def subfreq(n, a):
    count = {}
    for i in a:
        if(a in count):
            count[a] += 1
        else:
            count[a] = 1
    arr = [0]*n
    start = 1
    dash = 1
    mod = 1000000007
    prev = a[-1]
    a.sort()
    for i in range(len(a)-2, -1, -1):
        if(a[i]==a[i+1]):
            dash = (dash*2)%mod
            start = (start + dash)%mod
        else:
            arr[a[i+1]-1] = start
            prev = a[i]
            dash = (dash*2)%mod
            start = dash
    arr[a[0]-1] = start
    for i in range(len(arr)-1):
        if(count[i+1]<count[i+2] and count[i+1]!=0):
            arr[i]-=1
            arr[i+1]+=1
    return arr

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(*subfreq(n, a))
