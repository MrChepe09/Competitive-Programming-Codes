def ringroad(n, m, a):
    res = 0
    prev = 1
    for i in a:
        if(i>prev):
            res+= i-prev
            prev = i
        elif(i<prev):
            res += (n-prev)+i
            prev = i
    return res


n, m = map(int, input().split())
a = list(map(int, input().split()))
print(ringroad(n, m, a))