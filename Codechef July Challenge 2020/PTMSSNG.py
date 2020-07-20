def mispoint(n, p):
    dictia = set()
    dictib = set()
    for i in range(len(p)):
        if(p[i][0] in dictia):
            dictia.remove(p[i][0])
        else:
            dictia.add(p[i][0])
    for i in range(len(p)):
        if(p[i][1] in dictib):
            dictib.remove(p[i][1])
        else:
            dictib.add(p[i][1])
    res = [0, 0]
    for i in dictia:
        res[0] = i
        break
    for j in dictib:
        res[1] = j
        break

    return res
    

test = int(input())
for i in range(test):
    n = int(input())
    p = []
    for i in range((4*n)-1):
        a, b = map(int, input().split())
        p.append([a, b])
    print(*mispoint(n, p))
