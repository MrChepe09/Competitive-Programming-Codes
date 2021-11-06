def problem(n):
    ans = []
    new = []
    for i in range(n):
        new.append("(")
        new.append(")")
    ans.append(list(new))
    while(True):
        if(len(ans)==n):
            break
        for i in range(2, len(new)):
            if(new[i]=="("):
                new[1], new[i] = new[i], new[1]
                ans.append(list(new))
                new[1], new[i] = new[i], new[1]
    return ans
        
test = int(input())
for i in range(test):
    n = int(input())
    ans = problem(n)
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end="")
        print()
