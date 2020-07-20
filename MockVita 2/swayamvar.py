def wedding(n, w, g):
    count = 0
    drink = {}
    for i in g:
        if(i in drink):
            drink[i] += 1
        else:
            drink[i] = 1
    #print(drink)
    for i in w:
        if(drink[i]!=0):
            drink[i]-=1
            count+=1
        else:
            return n-count
    return n-count

n = int(input())
w = input()
g = input()
print(wedding(n, w, g))
