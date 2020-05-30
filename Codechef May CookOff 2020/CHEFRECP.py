def chefrecp(n, a):
  dicti = {}
  for i in range(n):
    if(a[i] not in dicti):
      dicti[a[i]] = 1
    elif(a[i] in dicti):
      if(a[i] == a[i-1]):
        dicti[a[i]] += 1
      else:
        return "NO"
  done = []
  for i in dicti:
    if(dicti[i] not in done):
      done.append(dicti[i])
    else:
      return "NO"
  return "YES"


test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  print(chefrecp(n, a))
