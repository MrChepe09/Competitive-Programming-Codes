from math import sqrt
def parellelepiped(s1, s2, s3):
    a = sqrt((s1*s3)/s2)
    b = sqrt((s1*s2)/s3)
    c = sqrt((s2*s3)/s1)

    return int(4*(a+b+c))

a, b, c = map(int, input().split())
print(parellelepiped(a, b, c))