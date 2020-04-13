from random import randint
def sbseq(N, a):
  temp = []
  count = 0
  temp1 = []
  for j in range(0, N):
    if(abs(a[j])%4==0):
      temp.append(j)
      temp1.append(4)
    elif(abs(a[j])%4==2):
      temp.append(j)
      temp1.append(2)

  n = len(temp)
  s, e = 0, N-1
  if(n==1):
    if(temp1[0]==2):
      count += ((e-temp[0]+1)*(temp[0]-s+1))
  if(n>=2):
    d = 0
    if(temp1[d]==2):
      count+= ((temp[d+1]-temp[d])*(temp[d]-s+1))
    for d in range(1, n-1):
      if(temp1[d] == 2):
        count+=((temp[d+1]-temp[d])*(temp[d]-temp[d-1]))
    d = n-1
    if(temp1[d]==2):
      count+= ((e-temp[d]+1)*(temp[d]-temp[d-1]))

  ans = ((N*(N+1))/2)-count
  return int(ans)
      

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(sbseq(n, a))
