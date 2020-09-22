def evenodd(n, k):
    if(n%2==1):
        odd = (n//2)+1
    else:
        odd = n//2
    if(k<=odd):
        return 1+(2*(k-1))
    else:
        return 2*(k-odd)

n, k = map(int, input().split())
print(evenodd(n, k))