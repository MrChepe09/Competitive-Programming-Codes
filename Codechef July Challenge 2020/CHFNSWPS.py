def pre(da, db, t):
    for i in range(len(a)):
        if a[i] in da:
            da[a[i]] += 1
        else:
            da[a[i]] = 1
    for i in range(len(b)):
        if b[i] in db:
            db[b[i]] += 1
        else:
            db[b[i]] = 1

    for i in range(len(a)):
        if a[i] in t:
            t[a[i]] += 1
        else:
            t[a[i]] = 1
    for i in range(len(b)):
        if b[i] in t:
            t[b[i]] += 1
        else:
            t[b[i]] = 1
            
def chefswaps(n, a, b):
    da = {}
    db = {}
    t = {}
    res = 0

#Dictionary preprepare
    pre(da, db, t)
#-------------------
   
#Check for invalid inputs
    #print(da, db, t)
    for i in t:
        if(t[i]%2==1):
            return -1
#---------------------
        
# Calculate Answer
    diff = {}
    #print(t)
    for i in t:
        counta = 0
        countb = 0
        if i in da:
            counta = da[i]
        if i in db:
            countb = db[i]
        if(counta != countb):
            diff[i] = int(abs(counta-countb)/2)
    #print(diff)
    #Answer is 0       
    if(len(diff)==0):
        return 0

    #Answer is not 0
    #print(diff)
    ans = []
    for i in diff:
        for j in range(diff[i]):
            ans.append(i)

    mini = min(t)
    ans.sort()
    #print(ans)
    #print(mini)
    for i in range(int(len(ans)/2)):
        if(ans[i] >= 2*mini):
            res += 2*mini
        else:
            res += ans[i]
    return res

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(chefswaps(n, a, b))
