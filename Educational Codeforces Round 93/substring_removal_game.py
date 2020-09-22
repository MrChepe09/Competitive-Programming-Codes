def substring(a):
    c = []
    count = 0
    for i in range(len(a)):
        #print(a[i], count)
        if (i=='0' and a[i]=='1'):
            count=1
            continue
        elif (a[i]=='1' and a[i-1]=='1'):
            count+=1
        elif (a[i]=='1' and a[i-1]=='0'):
             count = 1
        elif (a[i]=='0' and count>0):
            c.append(count)
            count = 0
    if(count!=0):
        c.append(count)
    c.sort(reverse=True)
    ans = 0
    #print(c)
    for i in range(0, len(c), 2):
        ans+=c[i]
    return ans


test = int(input())
for i in range(test):
    s = input()
    print(substring(s))
