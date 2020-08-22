def evenodd(a, b, k):
    mod = 1000000007
    if(a%2==0 and b%2==0):
        count = (b-a)+1
        even = (count//2)+1
        odd = count//2
        
    elif(a%2==1 and b%2==1):
        count = (b-a)+1
        odd = (count//2)+1
        even = count//2
        
    elif(a%2==1 and b%2==0):
        count = (b-a)+1
        odd = count//2
        even = count//2

    elif(a%2==0 and b%2==1):
        count = (b-a)+1
        odd = count//2
        even = count//2

    total = ((even+odd)*k)%mod

    return total

a, b = map(int, input().split())
k = int(input())
print(evenodd(a, b, k))
