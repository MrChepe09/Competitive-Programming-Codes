def problem(n, a):
  ans1 = []
  ans2 = []
  dicti = {}
  for i in a:
    if(i in dicti):
      dicti[i] += 1
    else:
      dicti[i] = 1
  for i in dicti:
    if(dicti[i]>2):
      return "NO"
    elif(dicti[i]==1):
      ans1.append(i)
      dicti[i]-=1
    elif(dicti[i]==2):
      ans1.append(i)
      dicti[i] -= 1
  for i in dicti:
    if(dicti[i]==1):
      ans2.append(i)
  ans1.sort()
  ans2.sort(reverse=True)
  if(len(ans2)!=0 and ans1[-1] == ans2[0]):
    return "NO"
  
  #print(ans1, ans2)
  return ans1+ans2

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  p = problem(n, a)
  if(p=="NO"):
    print(p)
  else:
    print("YES")
    print(*p)
