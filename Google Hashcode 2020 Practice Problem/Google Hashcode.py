fin = open('e_also_big.in', 'r')  #input file
fout = open('test.out', 'w')  #output file
ans = []
a, b = (fin.readline().strip('\n').split())
a = int(a)
b = int(b)
n1 = list(map(int, fin.readline().strip('\n').split()))
for i in range(b-1, -1, -1):
  if(a>n1[i]):
    a = a-n1[i]
    ans.append(i)
  elif(a==n1[i]):
    ans.append(i)
    break
  else:
    pass
ans.reverse()
piz= " ".join([str(num) for num in ans])
fout.write(str(len(ans))+'\n')
fout.write(piz)
fin.close()
fout.close()
