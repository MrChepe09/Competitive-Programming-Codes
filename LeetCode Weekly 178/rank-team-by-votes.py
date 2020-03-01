ranks = list(input().split())
for i in range(len(ranks[0])):
  dicti = {}
  for j in range(0, len(ranks)):
    if(ranks[j][i] not in dicti):
      dicti[ranks[j][i]] = 1
    elif(ranks[j][i] in dicti):
      dicti[ranks[j][i]] += 1
  print(dicti)
