def jeff(n, a):
    dicti = {}
    for i in range(n):
        #print(dicti)
        if(a[i] not in dicti):
            dicti[a[i]] = [i, 0, 0]
        else:
            if(dicti[a[i]][1]!=0):
                if(dicti[a[i]][2] == i-dicti[a[i]][0]):
                    dicti[a[i]][0] = i
                    dicti[a[i]][1] += 1
                else:
                    #print(dicti, i-dicti[a[i]][0])
                    dicti[a[i]][2] = -1
                    #print(h)
            else:
                dicti[a[i]][2] = i-dicti[a[i]][0]
                dicti[a[i]][0] = i
                dicti[a[i]][1] += 1
    ans = {}
    for i in dicti:
        if(dicti[i][2]!=-1):
            ans[i] = dicti[i][2]
    #print(dicti)
    return ans

n = int(input())
a = list(map(int, input().split()))
ans = jeff(n, a)
print(len(ans))
g = sorted(ans)
for i in g:
    print(str(i)+" "+str(ans[i]))