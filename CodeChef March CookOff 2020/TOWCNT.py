def tower(h, n, a):
  ans = []
  for t in range(0, len(a)):
    maxhf1 = 0
    maxhf0 = 0
    maxhb1 = 0
    maxhb0 = 0
    countf1 = 0
    countf0 = 0
    countb1 = 0
    countb0 = 0
    for z in range(0, len(a)):
      if(t!=z):
        if(a[z][1]>a[t][1]):
          if(a[z][0] == 1):
            if(a[z][2]>maxhf1):
            #print(maxh1)
              countf1+=1
              maxhf1 = max(maxhf1, a[z][2])
          
          elif(a[z][0] == 0):
            if(a[z][2]>maxhf0):
              countf0+=1
              maxhf0 = max(maxhf0, a[z][2])
        else:
          if(a[z][0] == 1):
            if(a[z][2]>maxhb1):
            #print(maxh1)
              countb1+=1
              maxhb1 = max(maxhb1, a[z][2])
          
          elif(a[z][0] == 0):
            if(a[z][2]>maxhb0):
              countb0+=1
              maxhb01 = max(maxhb0, a[z][2])
    ans.append(countf0+countf1+countb0+countb1)
  return ans

test = int(input())
for i in range(test):
  h, n = map(int, input().split())
  a = []
  for j in range(n):
    t = list(map(int, input().split()))
    if(t[0] == 1):
      t[2] = h-t[2]
    a.append(t)
  print(tower(h, n, a))
