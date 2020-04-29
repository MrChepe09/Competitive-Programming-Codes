def multiple2019(n):
  n = str(n)
  count = 0
  for i in range(0, len(n)-4):
    for j in range(i+4, len(n)+1):
      if(int(n[i:j])%2019==0):
        count +=1
  return count
n = int(input())
print(multiple2019(n))
