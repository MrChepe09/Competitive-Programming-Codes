def dubstep(s):
    s = s.replace('WUB', '.')
    #print(s)
    res = []
    temp = []
    i = 0
    while(i<len(s)):
        if(s[i]=='.'):
            fi = ''.join(temp)
            if(fi!=''):
                res.append(fi)
                res.append(" ")
                temp = []
        else:
            temp.append(s[i])
        i+=1
    if(s[-1]!='.'):
        fi = ''.join(temp)
        res.append(fi)
    ans = ''.join(res)
    return ans


s = input()
print(dubstep(s))