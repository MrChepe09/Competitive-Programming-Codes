def middle(arr, n, result):
    f = False
    result[1] = arr[0]
    for i in range(1, n):
        result[i+1] = result[i] + arr[i]

        if arr[i-1]%2!=0:
            result[i+1] -=1
        if f == True:
            if arr[i-2]%2!=0:
                result[i+1]+=1
            else:
                result[i+1]-=1
            f= False
        if arr[i]==1:
            f = True
    return result
            
def last(arr, n, result):
    result[1] = arr[0]
    for i in range(1, n-1):
        result[i+1] = (result[i]+arr[i])
        if (arr[i-1]%2!=0):
            result[i+1] = result[i+1]-1
    if n>1:
        result[n] = result[n-1]+arr[n-1]
    if arr[n-2]%2!=0:
        result[n] -= 1
    return result

mod = 1000000007
test = int(input())
for i in range(test):
    n = int(input())
    arr = list(map(int, input().split()))
    result = [0 for _ in range(n+1)]
    if arr[n-1]==1:
        result = last(arr, n, result)
    elif(arr[0]!=1):
        result = middle(arr, n, result)
    q = int(input())
    for i in range(q):
        r = int(input())
        ind = r//n
        ans = 0
        if n==1:
            if arr[0]%2==0:
                ans = ((arr[0]-1)%mod*(r-1)%mod)%mod
                ans = (ans%mod + arr[0]%mod)%mod
            else:
                ans = (arr[0]%mod*r%mod)%mod
        elif arr[0]==1:
            if r<=n:
                ans = 1
            elif(r%n==1 or r%n==0):
                ans = ind%mod
            elif r>n:
                ans = (ind%mod + 1)%mod
        elif arr[n-1]==1:
            ans = ((ind)%mod*(result[n])%mod)%mod
            p = int(r%mod-(ind)%mod*(n)%mod)%mod
            ans = (ans%mod + result[p]%mod)%mod
        else:
            ans = ((ind)%mod*(result[n])%mod)%mod
            if arr[n-1]%2==0:
                if r%n==0:
                    ans = ((ans%mod)-(ind-1)%mod)%mod
                else:
                    ans = ((ans)%mod-(ind)%mod)%mod
            p = int((r%mod)-(ind)%mod*(n)%mod)%mod
            ans = (ans%mod + result[p]%mod)%mod
        print(ans)
