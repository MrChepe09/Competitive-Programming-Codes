def molecules(s):
    global i
    global mass
    stack = []
    while(i<len(s)):
        if(s[i]=='H' or s[i]=='O' or s[i] == 'C'):
            stack.append(mass[s[i]])
            i+=1
        elif(s[i].isdigit()):
            di = stack.pop()
            stack.append(di*int(s[i]))
            i+=1
        elif(s[i]=='('):
            i+=1
            stack.append(molecules(s))
        elif(s[i]==')'):  
            i+=1
            return sum(stack)
    return sum(stack)

s = input()
i = 0
mass = {'C': 12, "O": 16, "H": 1}
print(molecules(s))