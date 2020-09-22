def compiler(s):
    ans = 0
    t = 0
    for i in range(len(s)):
        if(s[i]=='<'):
            t+=1
        else:
            t-=1
            if(t==0):
                ans = max(ans, i+1)
            elif(t<0):
                break
    return ans

test = int(input())
for i in range(test):
    s = input()
    print(compiler(s))