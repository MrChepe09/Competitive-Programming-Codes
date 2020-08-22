def factor(n, a):
    t1 = []
    t2 = []
    t3 = []
    for i in a:
        if(i%3==0):
            t1.append(i)
        elif(i%3==1):
            t2.append(i)
        else:
            t3.append(i)
    cont1 = len(t2)
    cont2 = len(t3)
    if(len(t1)==0 and cont1!=0 and cont2!=0):
        return "No"
    if(len(t1)<=cont1+cont2+1):
        return "Yes"
    else:
        return "No"
            
    
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(factor(n, a))
