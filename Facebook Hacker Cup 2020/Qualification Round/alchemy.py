def alchemy(n, s):
    counta = s.count('A')
    countb = s.count('B')
    if(abs(counta-countb)==1):
        return "Y"
    else:
        return "N"


fin = open('alchemy_input.txt', 'r')
fout = open('alchemy.txt', 'w')

test = int(fin.readline().strip('\n'))
for i in range(test):
    n = int(fin.readline().strip('\n'))
    s = fin.readline().strip('\n')
    ans = alchemy(n, s)
    dire = "Case #"+str(i+1)+': '
    fout.write(dire)
    fout.write(ans)
    fout.write('\n')
fin.close()
fout.close()
