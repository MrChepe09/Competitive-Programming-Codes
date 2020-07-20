def maxand(n, k, a):
  maxele = bin(max(a))[2:]
  maxa = [0]*len(maxele)
  print(maxele)
  for i in range(n):
    binary = bin(a[i])[2:]
    print(binary)
    for j in range(len(binary)):
      start = len(maxa)-1
      if(binary[j]==1):
        maxa[start] += 1
      start-=1
  return maxa
    

test = int(input())
for i in range(test):
  n, k = map(int, input().split())
  a = list(map(int, input().split()))
  print(maxand(n, k, a))
