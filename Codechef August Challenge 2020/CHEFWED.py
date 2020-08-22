def unique(n, a):
    done = []
    count = 1
    done.append(a[0])
    for i in range(1, n):
        if(a[i] in done):
            count += 1
            done = []
        done.append(a[i])
    return count

def duplicate(i, j, a):
    count = 0
    done = {}
    for i in range(i, j):
        if(a[i] in done):
            done[a[i]] += 1
        else:
            done[a[i]] = 1
    for i in done:
        if(done[i] > 1):
            count += done[i]
    return count
        

def wedding(n, k, a):
    a1 = unique(n, a)*k
    a2 = 0
    done = []
    a2 = duplicate(0, n, a)
    a2 += k
    a3 = float('inf')
    for i in range(n-1):
        j = i+1
        b1 = duplicate(0, i+1, a)
        b2 = duplicate(j, n, a)
        table = b1+k+b2+k
        if(table<a3):
            a3 = table
    #print(a1, a2, a3)
    return min(a1, a2, a3)

    
test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    print(wedding(n, k, a))
