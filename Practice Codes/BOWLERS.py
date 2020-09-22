def bowlers(n, k, l):
    bowlers = []
    ans = []
    for i in range(1, k+1):
        bowlers.append(i)
    if(k*l<n):
        return -1
    if(k==1 and n!=1):
        return -1
    while(n>0):
        if(len(bowlers)<=n):
            ans += bowlers
            n-=len(bowlers)
        else:
            for i in range(n):
                ans.append(bowlers[i])
                n-=1
    return ' '.join(map(str, ans))
        
test = int(input())
for i in range(test):
    n, k, l = map(int, input().split())
    print(bowlers(n, k, l))
