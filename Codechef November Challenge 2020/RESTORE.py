def seive(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    primes = []
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    for p in range(2, n+1): 
        if prime[p]: 
            primes.append(p)
    return primes

def restore(n, a, p):
    for i in range(n):
        a[i] = p[a[i]-1]
    return a

test = int(input())
p = seive(1350500)
#print(len(p))
for i in range(test):
    n = int(input())
    a = list(map(int, input().split()))
    print(*restore(n, a, p))
