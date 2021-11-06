def dancemoves(a, b):
    if(b<a):
        return abs(a-b)
    else:
        dis = abs(b-a)
        if(dis%2==0):
            return dis//2
        else:
            return (dis//2)+2

test = int(input())
for i in range(test):
    a, b = map(int, input().split())
    print(dancemoves(a, b))
