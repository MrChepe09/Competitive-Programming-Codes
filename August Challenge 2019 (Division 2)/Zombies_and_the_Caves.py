test_cases = int(input())
for i in range(test_cases):
  caves = int(input())
  radiation = [0]*caves
  caves_rad = [int(i) for i in input().split()]
  zombies = [int(i) for i in input().split()]
  for j in range(caves):
    for k in range(j-caves_rad[j], (j+caves_rad[j]+1)):
      if(k>=0 and k<caves):
        radiation[k] += 1
  for z in range(caves):
    if zombies[z] in radiation:
      index_z = radiation.index(zombies[z])
      radiation[index_z] = -1
    else:
      break

  if(z==caves-1):
    print("YES")
  else:
    print("NO")
  
