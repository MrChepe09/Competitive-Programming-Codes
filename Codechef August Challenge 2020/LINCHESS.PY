def chess(n, c, a):
    win = 0
    mini = float('inf')
    for i in a:
        if(c%i==0):
            if(c//i < mini):
                mini = c//i
                win = i
    if(win == 0):
        return -1
    return win


test = int(input())
for i in range(test):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    print(chess(n, c, a))
