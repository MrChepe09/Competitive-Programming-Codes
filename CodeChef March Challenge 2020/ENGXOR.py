from sys import stdin, stdout

  
test = int(stdin.readline())
#test = int(input())
for i in range(test):
  even = 0
  odd = 0
  n, q = map(int, stdin.readline().split())
  nlist = list(map(int, stdin.readline().split()))
  for k in nlist:
    z = bin(k).count('1')
    if(z%2==0):
        even += 1
    else:
        odd += 1
  for j in range(q):
    p = int(stdin.readline())
    #p = int(input())
    if(bin(p).count('1')%2==0):
        stdout.write(str(even)+' '+str(odd)+'\n')
    else:
        stdout.write(str(odd)+' '+str(even)+'\n')
    #stdout.write(str(even)+' '+str(odd))
    
    
  
