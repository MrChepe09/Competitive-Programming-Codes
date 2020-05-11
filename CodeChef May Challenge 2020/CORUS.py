def isolation(sd, c):
  count = 0
  for k in sd:
    if(sd[k] > c):
      count+=(sd[k]-c)
  return count

test = int(input())
for i in range(test):
  n, q = map(int, input().split())
  s = input()
  sd = {}
  for i in s:
    if(i in sd):
      sd[i] += 1
    else:
      sd[i] = 1
  for j in range(q):
    c = int(input())
    print(isolation(sd, c))
