def lapin(s):
    if(len(s)%2==0):
        a = s[:len(s)//2]
        b = s[len(s)//2:]
        #print(a, b)
    else:
        a = s[:len(s)//2]
        b = s[(len(s)//2)+1:]
        #print(a, b)
    ad = {}
    bd = {}
    for i in a:
        if(i in ad):
            ad[i]+=1
        else:
            ad[i] = 1
    for i in b:
        if(i in bd):
            bd[i]+=1
        else:
            bd[i] = 1
    if(ad==bd):
        return "YES"
    else:
        return "NO"
        

test = int(input())
for i in range(test):
    s = input()
    print(lapin(s))