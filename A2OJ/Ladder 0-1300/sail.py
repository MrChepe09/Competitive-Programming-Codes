def sail(s, ss, se, es, ee):
    x = 0
    y = 0
    if ss>es:
        x = ['W', ss-es]
    elif es>ss: 
        x = ['E', es-ss]

    if se>ee:
        y = ['S', se-ee]
    elif ee>se:
        y = ['N', ee-se]

    if x==0:
        i = 0
        while i<len(s):
            if s[i] == y[0]:
                y[1]-=1
            
            if y[1]==0:
                return i+1
            i+=1
        return -1
    elif y==0:
        i = 0
        while i<len(s):
            if s[i] == x[0]:
                x[1]-=1

            if x[1] == 0:
                return i+1
            i+=1
        return -1
    else:
        i = 0
        while i<len(s):
            if(s[i] == x[0] and x[1] != 0):
                x[1]-=1
            elif(s[i] == y[0] and y[1] != 0):
                y[1] -= 1

            if x[1] == 0 and y[1]==0:
                return i+1
            i+=1
        return -1

t, ss, se, es, ee = map(int, input().split())
s = input()
print(sail(s, ss, se, es, ee))