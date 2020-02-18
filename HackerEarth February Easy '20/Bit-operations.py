a, b = input().split()
a = int(a)
b = int(b)
arr = [0] * a
for i in range(b):
  summ = 0
  xor = 0
  ll = []
  ll = [int(j) for j in input().split()]
  if(ll[0]==1):
    for k in range(ll[1]-1, ll[2]):
      arr[k] = arr[k] | ll[3]
  elif(ll[0]==2):
    for k in range(ll[1]-1, ll[2]):
      arr[k] = arr[k] & ll[3]
  elif(ll[0]==3):
    for k in range(ll[1]-1, ll[2]):
      arr[k] = arr[k] ^ ll[3]
  elif(ll[0]==4):
    for k in range(ll[1]-1, ll[2]):
      summ = summ + arr[k]
    print(summ)
  elif(ll[0]==5):
    for k in range(ll[1]-1, ll[2]):
      xor = xor ^ arr[k]
    print(xor)
