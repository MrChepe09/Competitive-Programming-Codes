test_cases = int(input())
for i in range(test_cases):
  caves = int(input())
  radiation = [0]*caves
  caves_rad = [int(i) for i in input().split()]
  zombies = [int(i) for i in input().split()]
  for j in range(caves):
    left = max(0, j-caves_rad[j])
    right = min(caves-1, j+caves_rad[j])
    for k in range(left, right+1):
      radiation[k] += 1
  zombies.sort()
  radiation.sort()
  if(zombies==radiation):
    print("YES")
  else:
    print("NO")
  
