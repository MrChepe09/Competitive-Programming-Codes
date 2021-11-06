def testmatch(r):
    ind = 0
    eng = 0
    for i in r:
        if(i==1):
            ind+=1
        elif(i==2):
            eng += 1
    if(ind==eng):
        return "DRAW"
    elif(ind>eng):
        return "INDIA"
    else:
        return "ENGLAND"
    

test = int(input())
for i in range(test):
    r = list(map(int, input().split()))
    print(testmatch(r))
