def present(n):
    ans = []
    start = 0
    curr = n
    for i in range(n+1):
        temp = []
        for j in range(curr):
            temp.append(' ')
        for j in range(start+1):
            temp.append(j)
        for j in range(start-1, -1, -1):
            temp.append(j)
        curr-=1
        start+=1
        ans.append(temp)
    sna = ans[:-1]
    sna.reverse()
    ans+=sna
    return ans

n = int(input())
ans = present(n)
for i in range((n*2)+1):
    print(*ans[i])