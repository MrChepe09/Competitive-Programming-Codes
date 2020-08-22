def petya(a, b):
    a = a.lower()
    b = b.lower()
    for i in range(len(a)):
        if(a[i]>b[i]):
            #print(a[i], b[i])
            return 1
        elif(a[i]<b[i]):
            return -1
    return 0


a = input()
b = input()
print(petya(a, b))