def nsl(n, a):
    stack = []
    res = []
    for i in range(n):
        if(len(stack)==0):
            res.append(-1)
        elif(stack[-1]<a[i]):
            res.append(stack[-1])
        elif(len(stack)>0 and stack[-1]>=a[i]):
            while(len(stack)>0 and stack[-1]>=a[i]):
                stack.pop()
            if(len(stack)==0):
                res.append(-1)
            else:
                res.append(stack[-1])
        stack.append(a[i])
    return res

n = int(input())
a = list(map(int, input().split()))
print(*nsl(n, a))