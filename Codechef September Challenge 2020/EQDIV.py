def equal(n, k):
    counta = n**k
    countb = 0
    a = [1]
    n-=1
    while(n>0):
        if(counta<countb):
            counta+=(n**k)
            a.append(1)
        else:
            countb+=(n**k)
            a.append(0)
        n-=1
    a.reverse()
    return a, abs(counta-countb)
        
    

k = int(input())
test = int(input())
for i in range(test):
    n = int(input())
    ans1, ans2 = equal(n, k)
    print(ans2)
    print(''.join(map(str, ans1)))
