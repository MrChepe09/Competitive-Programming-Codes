def prefix(s, k, x):
  ans = []
  for j in range(len(s)):
    if(s[j] in ans and ans.count(s[j])==x and k==0):
      break
    elif(s[j] in ans and ans.count(s[j])==x and k!=0):
      k -= 1
    else:
      ans.append(s[j])
  return(len(ans))
      

test = int(input())
for i in range(test):
  s = input()
  k, x = map(int, input().split())
  print(prefix(s, k, x))
