def check(a):
    out = 0
    for i in range(len(a)):
        count = 1000
        num = 0
        for j in range(i, len(a)):
            count = min(count, a[j])
            num += 1
            if(count>=num):
                out = max(out, num)
    print(out)
    return out
            
def brickwall(n, a):
    count = 0
    arr = []
    new = []
    num = 1000
    #print(a)
    for i in range(n):
        for j in range(n):
            if(a[i][j]=='D'):
                count += 1
        new.append(count)
        count = 0
    arr.append(new)
    new = []
    
    for i in range(n):
        for j in range(n):
            if(a[j][i]=='D'):
                count += 1
        new.append(count)
        count = 0
    arr.append(new)
    print(arr)
    count = 1000
    num = 0
    out = 0
    for i in range(len(arr)):
        out = max(out, check(arr[i]))
    return out

n = int(input())
arr = []
for i in range(n):
    a = input().split()
    arr.append(a)
print(brickwall(n, arr))
