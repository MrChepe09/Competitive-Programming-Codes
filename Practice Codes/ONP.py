def expression(s):
    t = 0
    stack = []
    res = []
    while(t<len(s)):
        if(s[t]=='+' or s[t]=='-' or s[t]=='*' or s[t]=='^' or s[t]=='/'):
            stack.append(s[t])
        elif(s[t]==')'):
            res.append(stack.pop())
        elif(s[t]=='('):
            pass
        else:
            res.append(s[t])
        t+=1
    return ''.join(res)


test = int(input())
for i in range(test):
    s = input()
    print(expression(s))