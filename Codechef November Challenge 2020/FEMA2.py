#P = k + 1 - abs(j-i) - s
def checkpower(i, j, k, s):
    return (k+1)-abs(i-j)-s
    
def magnets(n, k, s):
    i = 0
    j = 0
    con = 0
    res = 0
    while(i<n and j<n):
        
        if s[i] == 'M':
            if s[j] == 'I':
                if i<j:
                    for g in range(i, j):
                        if s[g] == ":":
                            con += 1

                elif i>j:
                    for g in range(j, i):
                        if s[g] == ":":
                            con += 1
    
                power = checkpower(i, j, k, con)
                #print(s[i], s[j], i, j, power, k, con)
                if power>0:
                    i+=1
                    j+=1
                    res+=1
                    con = 0
                else:
                    if i>j:
                        j+=1
                        con = 0
                    else:
                        i+=1
                        con = 0
            elif s[j] == 'X':
                i=j
                i+=1
                j+=1
                con = 0
            else:
                j+=1
        elif s[i] == 'X':
            j=i
            i+=1
            j+=1
            con = 0
        else:
            i+=1
    return res
                    
test = int(input())
for i in range(test):
    n, k = map(int, input().split())
    s = input()
    print(magnets(n, k, s))
