def isprime(n):
    if(n==1):
        return False
    for i in range(2, int(n**0.5)+1):
        if(n%i==0):
            return False
    return True

def predict(n, m):
    for i in range(n+1, m+1):
        #print(isprime(i))
        if(isprime(i)):
            if(i==m):
                return "YES"
            else:
                return "NO"
    return "NO"

n, m = map(int, input().split())
print(predict(n, m))