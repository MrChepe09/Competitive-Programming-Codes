from itertools import combinations
test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  binary = input()
  li = [0]
  ans = 0
  x = 0
  count = 0
  dd = 0
  for j in range(a-1, -1, -1):
    if(binary[j]=='1'):
      #print(j, count)
      x += 2**count
  for j in range(a-1, -1, -1):
    if(binary[j]=='_'):
      if((x+sum(li))%b==0):
        ans += 1
      li.append(2**count)
      count +=1
      dd +=1
    else:
      count+=1
  #print(li)
  comb = combinations(li, dd)
  for t in list(comb):
    if((x+sum(t))%b==0):
      #print(x+sum(t))
      ans += 1
  print(ans)
