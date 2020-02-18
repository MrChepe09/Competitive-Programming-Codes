test = int(input())
for i in range(test):
  s = input()
  a = []
  b = []
  for j in range(len(s)):
    if(j<int(len(s)/2)):
      a.append(s[j])
    elif(j>int(len(s)/2)):
      b.append(s[j])
  if(len(s)%2==0):
    b.append(s[int(len(s)/2)])
  a.sort()
  b.sort()
  if(a==b):
    print("YES")
  else:
    print("NO")
