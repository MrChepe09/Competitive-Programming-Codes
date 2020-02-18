import math
fin = open('d_pet_pictures', 'r')  #input file
fout = open('test.out.txt', 'w')  #output file
r = int(fin.readline().strip('\n'))
p = 0
array = []
for i in range(r):
    n1 = list(map(str, fin.readline().strip('\n').split()))
    array.append(n1)
fin.close()
total = 0
for j in range(r):
    if array[j][0] == 'H':
        total += 1
    else:
        total += 0.5
ceil = int(math.ceil(total))
fout.write(str(ceil)+'\n')
k = 0
countk = 0

while p < (len(array)):
    if array[p][0] == 'V':
        countk = countk + 1
        if (countk % 2 == 1):
            for l in range(p+1, len(array)):
                if array[l][0] == 'V':
                    fout.write(str(p)+" "+str(l)+'\n')
                    break
        p = p + 1
    else:
        p = p + 1

while k < (len(array)):
    if array[k][0] == 'H':
        fout.write(str(k)+'\n')
        k = k + 1
    else:
        k = k + 1

fout.close()
        
