def garland(n, k, s):
  start = 0
  s = list(s)
  to = -1
  count = 0
  for j in range(n):
    if(s[j]=='1' and to==-1):
      to = j
    elif(to!=-1):
      if(j-k==to):
        if(s[j]=='0'):
          if(s[j:].count('1')==0):
            break
          count+=1
          #print(j)
        to = j
      else:
        if(s[j]=='1'):
          count+=1
          #print(j)
  return count

        
test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  s = input()
  print(garland(n, k, s))
