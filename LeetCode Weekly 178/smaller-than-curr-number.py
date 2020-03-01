test = int(input())
for i in range(test):
  no = list(map(int, input().split()))
  ans = []
  n = len(no)
  for j in range(n):
    count = 0
    for k in range(n):
      if(no[j]>no[k] and no.index(no[j])!= no.index(no[k])):
        count+=1
    ans.append(count)
  print(ans)
