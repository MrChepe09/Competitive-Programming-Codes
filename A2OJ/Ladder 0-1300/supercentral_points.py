def supercentral(n, a):
    count = 0
    for i in range(n):
        r = l = u = d = 0
        curr = a[i]
        for j in range(n):
            if(a[j][0]>curr[0] and a[j][1]==curr[1]):
                r+=1

            if(a[j][0]<curr[0] and a[j][1]==curr[1]):
                l+=1
            
            if(a[j][0]==curr[0] and a[j][1]>curr[1]):
                u+=1

            if(a[j][0]==curr[0] and a[j][1]<curr[1]):
                d+=1

        if(l>0 and r>0 and u>0 and d>0):
            count+=1
    return count


n = int(input())
arr = []
for i in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
print(supercentral(n, arr))