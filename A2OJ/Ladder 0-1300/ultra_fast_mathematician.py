def maths(a, b):
    new = []
    for i in range(len(a)):
        if(a[i]==b[i]):
            new.append('0')
        else:
            new.append('1')
    return ''.join(new)


a = input()
b = input()
print(maths(a, b))