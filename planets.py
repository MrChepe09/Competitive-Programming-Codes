def planets(r, v, n):
    for i in range(len(v)):
        v[i] = v[i]*n
        v[i] = v[i] % 360
    for i in range(1, len(v)):
        if v[i] != v[i-1]:
            return 'FALSE'
    return 'TRUE'
    

test = int(input())
for i in range(test):
    r = list(map(int, input().split()))
    v = list(map(int, input().split()))
    n = int(input())
    print(planets(r, v, n))
