def long(s):
    if(len(s)>10):
        s = s[0]+str(len(s)-2)+s[-1]
    return s

n = int(input())
for i in range(n):
    s = input()
    print(long(s))