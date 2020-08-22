def chefwars(d, c):
    while(c!=0):
        d-=c
        c = c//2
        if(d<=0):
            return 1
    return 0


test = int(input())
for i in range(test):
    d, c = map(int, input().split())
    print(chefwars(d, c))
