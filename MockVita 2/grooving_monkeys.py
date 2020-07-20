def monkeys(n, a):
    lista = a
    listb = [0]*len(a)
    count = 0
    while(listb!=a):
        count += 1
        listb = [0]*len(a)
        for i in range(len(a)):
            listb[a[i]-1] = lista[i]
        lista = listb
    return count
        
test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(monkeys(n, a))
