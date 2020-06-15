def matgame(n, m, mat):
  v = "Vivek"
  a = "Ashish"
  row = []
  column = []
  for i in range(n):
    for j in range(m):
      if(mat[i][j] == 1):
        row.append(i)
        column.append(j)
  count = 0
  for i in range(n):
    for j in range(m):
      if(mat[i][j] == 0):
        if((i not in row) and (j not in column)):
          count+=1
          row.append(i)
          column.append(j)
  if(count%2==0):
    return v
  else:
    return a
      


test = int(input())
for i in range(test):
  n, m = map(int, input().split())
  mat = []
  for i in range(n):
    a = list(map(int, input().split()))
    mat.append(a)
  print(matgame(n, m, mat))
