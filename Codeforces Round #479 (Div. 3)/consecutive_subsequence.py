def consecseq(n, a):
    global dp
    maxi = 0
    endind = 0
    endi = 0
    for i in range(len(a)):
        dp[a[i]] = dp[a[i]-1]+1
        if(dp[a[i]]>maxi):
            maxi = dp[a[i]]
            endind = i
            endi = a[i]
    return maxi, endind, endi
        
def arrayfind(endi, pos):
    global a
    if(pos<0):
        return
    if(a[pos]==endi):
        arrayfind(endi-1, pos-1)
        print(pos+1, end=" ")
    else:
        arrayfind(endi, pos-1)
    

n = int(input())
a = list(map(int, input().split()))
dp = [0]*200005
ans, ind, ele = consecseq(n, a)
print(ans)
arrayfind(ele-1, ind-1)
print(ind+1)
