def school(n, t, s):
    s = list(s)
    for i in range(t):
        a = [0]*len(s)
        for j in range(len(s)-1):
            if(s[j] == 'B' and s[j+1] == 'G' and a[j] == 0):
                a[j+1] = 1
                s[j], s[j+1] = s[j+1], s[j]
    return ''.join(s)

n, t = map(int, input().split())
s = input()
print(school(n, t, s))