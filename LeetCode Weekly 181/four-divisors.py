import math
nums = list(map(int, input().split()))
sumi = 0
for i in nums:
  suml = []
  count = 0
  for j in range(1, int(math.sqrt(i))+1):
    if(i%j==0):
      if(i/j == j):
        count+=1
        suml.append(j)
      else:
        count += 2
        suml.append(j)
        suml.append(i/j)
  if(count==4):
    sumi += sum(suml)
print(int(sumi))
    
