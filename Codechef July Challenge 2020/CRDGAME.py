def sumdig(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

def chefcard(n, a):
    chef = 0
    monty = 0
    for i in range(len(a)):
        c = sumdig(a[i][0])
        m = sumdig(a[i][1])
        if(c > m):
            chef += 1
        elif(c < m):
            monty += 1
        else:
            chef += 1
            monty += 1
    if(chef>monty):
        return [0, chef]
    elif(chef<monty):
        return [1, monty]
    else:
        return [2, monty]
    

test = int(input())
for i in range(test):
    n = int(input())
    a = []
    for i in range(n):
        s = list(map(int, input().split()))
        a.append(s)
    print(*chefcard(n, a))
