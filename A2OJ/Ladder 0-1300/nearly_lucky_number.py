def lucky(n):
    f = n.count('4')
    s = n.count('7')
    if(f+s==4 or f+s==7):
        return "YES"
    return "NO"

n = input()
print(lucky(n))