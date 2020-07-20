def adaking(n):
    res = [['.' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if(n != 0):
                n-=1
            else:
                res[i][j] = 'X'
        if(res[i][0] == 'X'):
            break
    res[0][0] = 'O'
    return res


test = int(input())
for i in range(test):
    n = int(input())
    ans = adaking(n)
    for i in range(8):
        for j in range(8):
            print(ans[i][j], end="")
        print()

