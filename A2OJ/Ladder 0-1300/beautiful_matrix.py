def matrix(x, y):
    return abs(2-x) + abs(2-y)

mat = []
for i in range(5):
    a = list(map(int, input().split()))
    if(1 in a):
        indx = i
        indy = a.index(1)
print(matrix(indx, indy))