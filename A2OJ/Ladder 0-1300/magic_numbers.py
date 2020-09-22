def magic(n):
    for i in range(len(n)):
        if(n[i]=='4'):
            if(i<1 or (n[i-1]!='1' and n[i-2]!='1')):
                return "NO"
        elif(n[i]!='4' and n[i]!='1'):
            return "NO"
    return "YES"


n = input()
print(magic(n))