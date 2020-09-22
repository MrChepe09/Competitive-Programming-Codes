def finxor():
    value = 0
    n = int(input())
    a = []
    for i in range(1, 21):
        print(str(1)+" "+str(1<<i))
        x = int(input())
        a.append(x)
    a.reverse()
    add = a[0]-n*(1<<20)
    if(add%2!=0):
        value+=1
    for i in range(1, len(a)):
        if(a[i]>=add):
            a[i] = n-(a[i]-add)
            a[i] = a[i]//(1<<(len(a)-i))
            a[i] = a[i]//2
        else:
            a[i] = n+(add-a[i])
            a[i] = a[i]//(1<<(len(a)-i))
            a[i] = a[i]//2


    for i in range(1, len(a)):
        if(a[i]%2!=0):
            value += 1<<(len(a)-i)
    
    print(str(2)+" "+str(value))

    res = int(input())
    return res

test = int(input())
for i in range(test):
    g = finxor()
    if(g==-1):
        break
