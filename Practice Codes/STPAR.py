def parade(n, a):
    stack = [0]
    start = 1
    i = 0
    while(i<n):
        #clsprint(a[i], start, stack)
        if(a[i]==start):
            start += 1
            i+=1
            continue
        else:
            if(stack[-1]==start):
                stack.pop()
                start+=1
                continue
            else:
                #print(stack[-1], a[i])
                if(stack[-1]<a[i] and stack[-1]!=0):
                    return "no"
                stack.append(a[i])
        i+=1
    return "yes"
            

while(True):
    n = int(input())
    if(n==0):
        break
    a = list(map(int, input().split()))
    print(parade(n, a))