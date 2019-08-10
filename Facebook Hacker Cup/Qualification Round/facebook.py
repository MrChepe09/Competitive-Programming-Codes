fin = open('leapfrog_ch_ (1).txt', 'r')  #input file
fout = open('test.out.txt', 'w')  #output file
r = int(fin.readline().strip('\n'))
for i in range(r):
    dot = 0
    b = 0
    n1 = str(fin.readline().strip('\n'))
    for j in range(len(n1)):
        if n1[j] == '.':
            dot = dot + 1
        elif n1[j] == 'B':
            b = b + 1
    if b >= dot and b != 0 and dot != 0:
        fout.write("Case #"+str(i+1)+": Y"+'\n')
    else:
        fout.write("Case #"+str(i+1)+": N"+'\n')
fin.close()
fout.close()
        
