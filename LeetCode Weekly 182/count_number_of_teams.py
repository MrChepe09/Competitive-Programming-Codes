def soldiers(rating):
  teams = 0
  for i in range(len(rating)-2):
    for j in range(i, len(rating)-1):
      for k in range(j, len(rating)):
        if(rating[i]<rating[j] and rating[j]<rating[k]):
          teams+=1
        elif(rating[i]>rating[j] and rating[j]>rating[k]):
          teams+=1
  return teams


aa = list(map(int, input().split()))
print(soldiers(aa))
