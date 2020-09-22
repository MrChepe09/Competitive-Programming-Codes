def football(s):
    count = 1
    for i in range(1, len(s)):
        if(s[i]==s[i-1]):
            count+=1
        else:
            count=1
        
        if(count==7):
            return "YES"
    return "NO"

s = input()
print(football(s))