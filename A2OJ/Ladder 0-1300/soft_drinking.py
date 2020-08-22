def softdrink(a):
    tlitre = a[2]*a[1]//a[-2]
    lime = a[3]*a[4]
    tsalt = a[-3]//a[-1]
    return min(tlitre, lime, tsalt)//a[0]

a = list(map(int, input().split()))
print(softdrink(a))