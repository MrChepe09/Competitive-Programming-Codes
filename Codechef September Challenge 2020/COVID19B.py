def check(n, v, i):
    global a
    check = [0 for _ in range(n)]
    time = [0 for _ in range(n)]
    check[i] = 1
    for j in range(i+1, n):
        if(a[j]<v):
            check[j] = 1
            time[j] = (i-j)/(a[j]-v)
    for j in range(i):
        if(a[j]>v):
            check[j] = 1
            time[j] = (i-j)/(a[j]-v)

    for j in range(n):
        if(check[j]==1):
            for k in range(j+1, n):
                if(a[j]-a[k] != 0):
                    tim = (k-j)/(a[j]-a[k])
                    if(a[k]<a[j] and tim>time[j]):
                        time[k] = tim
                        check[k] = 1
            for k in range(j):
                if(a[j]-a[k] != 0):
                    tim = (k-j)/(a[j]-a[k])
                    if(a[k]>a[j] and tim>time[j]):
                        time[k] = tim
                        check[k] = 1

    for j in range(n):
        if(check[j]==1):
            for k in range(j+1, n):
                if(a[j]-a[k] != 0):
                    tim = (k-j)/(a[j]-a[k])
                    if(a[k]<a[j] and tim>time[j]):
                        time[k] = tim
                        check[k] = 1
            for k in range(j):
                if(a[j]-a[k] != 0):
                    tim = (k-j)/(a[j]-a[k])
                    if(a[k]>a[j] and tim>time[j]):
                        time[k] = tim
                        check[k] = 1
            
    return sum(check)
                

def covid19b(n, a):
    ans = [1 for _ in range(n)]
    
    for i in range(len(a)):
        ans[i] += check(n, a[i], i)-1
    #print(ans)
        
    return str(min(ans))+" "+str(max(ans))

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(covid19b(n, a))
