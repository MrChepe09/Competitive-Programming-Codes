def joke(a, b, c):
    ab = a+b
    ab = list(ab)
    c = list(c)
    ab.sort()
    c.sort()
    if(ab==c):
        return "YES"
    else:
        return "NO"


a = input()
b = input()
c = input()
print(joke(a, b, c))