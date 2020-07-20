def orthodox(n, a):
    res = set() 
    total = (n*(n+1))//2
    pre = {0} 
  
    for x in a: 
        pre = {x | y for y in pre} | {x}
        #print(pre)
        res |= pre
        #print(res)
  
    if(len(res)==total):
        return "YES"
    return "NO"

test = int(input())
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(orthodox(n, a))
