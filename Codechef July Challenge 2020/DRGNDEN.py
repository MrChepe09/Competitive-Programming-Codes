def maxspice(a, b, h, d, k):
    if(k==1):
        cost = d[a-1]
        curr = h[a-1]
        ind = a-1
        for i in range(a-2, b-2, -1):
            if(h[i]>curr):
                curr = h[i]
                cost += d[i]
                ind = i
        if(ind!=(b-1)):
            return -1
    else:
        cost = d[b-1]
        curr = h[b-1]
        ind = b-1
        #print(b, a)
        for i in range(b, a):
            if(h[i]>curr):
                curr = h[i]
                cost += d[i]
                ind = i
        if(ind!=(a-1)):
            return -1
    #print(ind)
        
    return cost
    
def dragonden(h, d, c, p):
    if(c==p):
        return d[c-1]
    elif(c<p):
        return maxspice(p, c, h, d, 1)
    else:
        return maxspice(c, p, h, d, 2)
    
n, q = map(int, input().split())
h = list(map(int, input().split()))
d = list(map(int, input().split())) 
for i in range(q):
    t, c, p = map(int, input().split())
    if(t==1):
        d[c-1] = p
    else:
        print(dragonden(h, d, c, p))
