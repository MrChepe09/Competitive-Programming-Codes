test_cases = int(input())
total = 0
for i in range(test_cases):
  afilm = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
  profit = [0, 0, 0, 0]
  n = int(input())
  for k in range(n):
    a = [j for j in input().split()]
    if(a[0] == 'A'):
      afilm[0][int((int(a[1])/3)-1)] += 1
    elif(a[0] == 'B'):
      afilm[1][int((int(a[1])/3)-1)] += 1
    elif(a[0] == 'C'):
      afilm[2][int((int(a[1])/3)-1)] += 1
    elif(a[0] == 'D'):
      afilm[3][int((int(a[1])/3)-1)] += 1
  cost = 100
  ans = 0
  print(afilm)
  for e in range(0, 4):
    maxi = 0
    c = 0
    y = 0
    for w in range(0, 4):
      index(max(map(max, numbers)))
      if(afilm[w][e]>maxi):
        maxi = afilm[w][e]
        c=w
        y+=1
    profit[e] = maxi
    if(y!=0):
      afilm[c][1]=afilm[c][2]=afilm[c][3]=0
  profit.sort(reverse=True)
  print(profit)
  for e in range(0, 4):
    if(profit[e]==0):
      ans=ans-100
    else:
      ans=ans+(profit[e]*cost)
      cost = cost - 25
  print(ans)
  total += ans
print(total)
    
    
  
