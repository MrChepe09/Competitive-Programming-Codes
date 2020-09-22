from math import pow

def trumpcard(n, a):
    global mod
    maxi = max(a)
    turn = 1
    cmaxi = a.count(maxi)
    
    res = int(pow(2, n))%mod
    if(cmaxi%2==0):
        mini = min(cmaxi//2, cmaxi-cmaxi//2)
        for i in range(mini):
            turn = int(((turn%mod)*(cmaxi-i)%mod))%mod
            turn = int(((turn%mod) * (pow(i+1, mod-2)%mod)))%mod
        res -= ((pow(2, n-cmaxi)%mod)*(turn)%mod)%mod

    if(res<0):
        return (int(res)+mod)%mod
    return int(res)%mod


test = int(input())
mod = 1000000007
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    if(n==1):
        print(2)
        continue
    print(trumpcard(n, a))