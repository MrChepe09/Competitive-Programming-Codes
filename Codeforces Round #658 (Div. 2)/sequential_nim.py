def stones(n, a):
    f = "First"
    s = "Second"
    win = f
    if(a.count(1)==n):
        if(a.count(1)%2==0):
            return s
        else:
            return f
    for i in range(len(a)):
        if(a[i]==1):
            if(win==f):
                win = s
            else:
                win = f
        else:
            return win

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(stones(n, a))
