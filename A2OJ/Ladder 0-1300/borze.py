def borzecode(s):
    ans = []
    start = 0
    while(start!=len(s)):
        if(s[start] == '.'):
            ans.append(0)
            start += 1
        elif(s[start] == '-' and s[start+1] == '.'):
            ans.append(1)
            start += 2
        elif(s[start] == '-' and s[start+1] == '-'):
            ans.append(2)
            start += 2
    return ''.join(map(str, ans))

s = input()
print(borzecode(s))