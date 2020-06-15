def evenmatrix(n):
  ans = []
  tn = 0
  start = 1
  for k in range(n):
    temp = []
    for t in range(n):
      temp.append(start)
      start+=1
    if(tn==0):
      ans.append(temp)
      tn = 1
    else:
      ans.append(temp[::-1])
      tn = 0
  return ans


test = int(input())
for i in range(test):
  n = int(input())
  ans = evenmatrix(n)
  for j in ans:
    print(*j)
