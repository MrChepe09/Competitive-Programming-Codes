"""
ID: mrchepe09
LANG: PYTHON3
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

n = int(fin.readline())
names = {}
for i in range(n):
  a = fin.readline().strip('\n')
  names[a] = 0
for i in range(n):
  g = fin.readline().strip('\n')
  r, p = map(int, fin.readline().split())
  names[g] -= r
  t = 0
  if(p!=0):
    t = r//p
  for j in range(p):
    p1 = fin.readline().strip('\n')
    names[p1] += t
  names[g] += (r-(t*p))
for i in names:
  pri = (i+" "+str(names[i]))
  fout.write(pri+'\n')
fin.close()
fout.close()
