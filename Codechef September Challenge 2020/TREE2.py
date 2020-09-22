def tree2(n, a):
    a = set(a)
    res = 0
    for i in a:
        if(i!=0):
            res+=1
    return res

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(tree2(n, a))
