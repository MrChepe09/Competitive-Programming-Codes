def travel(n, inc, out):
    mat = [["N" for _ in range(n)] for _ in range(n)]
    for i in range(len(mat)):
        mat[i][i] = 'Y'
        if(out[i]=='Y'):
            for j in range(i-1, -1, -1):
                if(inc[j] == "Y" and out[j+1]=='Y'):
                    mat[i][j] = 'Y'
                else:
                    break
            for j in range(i+1, n):
                if(inc[j] == "Y" and out[j-1]=='Y'):
                    mat[i][j] = 'Y'
                else:
                    break
    return mat
    

f1 = open("travel_restrictions_input.txt", 'r')
f2 = open("answer1.txt", 'w')
test = int(f1.readline().strip('\n'))
for i in range(test):
    n = int(f1.readline().strip('\n'))
    inc = f1.readline().strip('\n')
    out = f1.readline().strip('\n')
    ans = travel(n, inc, out)
    g = "Case #"+str(i+1)+":"+'\n'
    f2.write(g)
    for j in ans:
        jn = ''.join(j)
        f2.write(jn+'\n')
f1.close()
f2.close()
