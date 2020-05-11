def triplesort(n, k, p):
  p = [0] + p
  count = 0
  sorte = [False]*(n+1)
  ans = []
  pairs = []
  for j in range(1, n+1):
    if(sorte[j]==True):
      continue
    if(p[j]==j):
      sorte[j] = True
      continue
    one = j
    triplets = []
    triplets.append(one)
    sorte[one] = True
    while(sorte[p[one]]!=True):
      triplets.append(p[one])
      one = p[one]
      sorte[one] = True
    tripsize = len(triplets)
    for z in range(tripsize-1, 1, -2):
      ans.append([triplets[z-2], triplets[z-1], triplets[z-0]])
      count+=1
    if(tripsize%2==0):
      pairs.append(triplets[0])
      pairs.append(triplets[1])
  
  if(len(pairs)%4==2):
    return -1
  else:
    for j in range(0, len(pairs), 4):
      ans.append([pairs[j+0], pairs[j+2], pairs[j+1]])
      count+=1
      ans.append([pairs[j+1], pairs[j+3], pairs[j+2]])
      count+=1

  if(count>k):
    return -1
  else:
    return ans
  

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  p = list(map(int, input().split()))
  z = triplesort(n, k, p)

  if(z==-1):
    print(-1)
  else:
    print(len(z))
    for j in range(len(z)):
      print(*z[j])
