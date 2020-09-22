def ngr(n, a):
    stack = []
    res = []
    for i in range(n-1, -1, -1):
        if(len(stack)==0):
            res.append(-1)
        elif(stack[-1]>a[i]):
            res.append(stack[-1])
        elif(len(stack)>0 and stack[-1]<=a[i]):
            while(len(stack)>0 and stack[-1]<=a[i]):
                stack.pop()
            if(len(stack)==0):
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(a[i])
    res.reverse()
    return res

n = int(input())
a = list(map(int, input().split()))
print(*ngr(n, a))