def cardgame(c, r):
    rick = 1
    chef = 1
    if(r%9==0):
        rick += (r//9)-1
    else:
        rick += r//9
    if(c%9==0):
        chef += (c//9)-1
    else:
        chef += c//9

    if(rick<=chef):
        return str(1)+" "+str(rick)
    else:
        return str(0)+" "+str(chef)

test = int(input())
for i in range(test):
    c, r = map(int, input().split())
    print(cardgame(c, r))
