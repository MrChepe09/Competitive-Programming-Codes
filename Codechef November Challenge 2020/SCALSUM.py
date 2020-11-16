def power(b, e): 
    if (e == 0):
        return 1 
  
    if (e == 1): 
        return b 
  
    f = power(b, e // 2); 
    f = (f * f) 
  
    if (e % 2 == 0): 
        return f
    else:
        return (b * f)
    
def scalsum(u, v, w, p):
    sum = 0
    mod = power(2, 32)
    while(u and v):
        sum = (sum%mod + ((w[u-1]%mod) * (w[v-1]%mod))%mod)%mod
        u = p[u]
        v = p[v]
    return int(sum)

n, q = map(int, input().split())
weight = list(map(int, input().split()))
parent = [0 for i in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    parent[v] = u
for i in range(q):
    u, v = map(int, input().split())
    print(scalsum(u, v, weight, parent))
