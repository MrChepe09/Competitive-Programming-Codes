def chatroom(s):
    a = ['h', 'e', 'l', 'l', 'o']
    j = 0
    i = 0
    while(i<len(s) and j<len(a)):
        if(s[i]==a[j]):
            j+=1
        i+=1
    if(j==len(a)):
        return "YES"
    return 'NO'
        

s = input()
print(chatroom(s))