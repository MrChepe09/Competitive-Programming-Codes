def problemB(n):
  ans = []
  even = 2
  odd = 1
  sumo = 0
  if(int(n/2)%2==1):
    return "NO"
  else:
    for i in range(int(n/2)):
      ans.append(even)
      even+=2
    sume = sum(ans)
    for i in range(int(n/2),n-1):
      ans.append(odd)
      sumo+=odd
      odd+=2
  ans.append(sume-sumo)
  return ans
  


test = int(input())
for i in range(test):
  n = int(input())
  ad = problemB(n)
  if(ad!='NO'):
    print("Yes")
    print(*ad)
  else:
    print("NO")
