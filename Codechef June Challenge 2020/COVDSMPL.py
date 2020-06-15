def covidsample(n, p):
  ans = [[0 for _ in range(n)] for _ in range(n)]
  add = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      print(1, 1, 1, i+1, j+1)
      mat = int(input())
      if(mat==-1):
        break
      add[i][j]=mat
      if(i==0 and j==0):
        ans[i][j] = mat
  print(add)
  for i in range(n):
    for j in range(n):
      if(i==0 and j>0):
        ans[i][j] = add[i][j]-add[i][j-1]
      elif(i>0 and j==0):
        ans[i][j] = add[i][j]-add[i-1][j]
      elif(i>0 and j>0):
        ans[i][j] = add[i][j]-add[i-1][j]-add[i][j-1]+add[i-1][j-1]
    
  return ans


test = int(input())
for i in range(test):
  n, p = map(int, input().split())
  ans = covidsample(n, p)
  if(ans==-1):
    break
  else:
    print(2)
    for j in ans:
      print(*j)
    z = int(input())
    if(z==-1):
      break
