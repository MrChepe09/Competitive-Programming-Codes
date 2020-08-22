def horseshoe(a):
    return len(a)-len(set(a))

a = list(map(int, input().split()))
print(horseshoe(a))