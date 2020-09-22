def binary_exponentiation(a, b):
    res = 1
    while(b>0):
        if b==0:
            return 1
        if(b%2==1):
            res *= a
            b-=1
        else:
            a*=a
            b=b//2
    return res


a, b = map(int, input().split())
print(binary_exponentiation(a, b))