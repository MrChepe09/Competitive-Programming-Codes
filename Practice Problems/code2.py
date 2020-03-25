line1 = input()
(m, n, k) = [int(x) for x in line1.split()]
grid = new_list = [[0 for i in range(n)] for j in range(m)]
total = 0
grid = []
for i in range(m):
  grid.append([int(x) for x in input().split()])
for i in range(len(grid)):
  for j in range(len(grid[i])):
    if grid[i][j] == 1:
      p = i
      q = j
      for z in range(1, k+1):
        ans = 0
        if(p+z<m and q+z<n and p-z>=0 and q-z>=0):
          u = p+z
          v = q+z
          w = p-z
          x = q-z
          if(grid[u][v] == 1 or grid[w][x] == 1 or grid[u][x] == 1 or grid[w][v] == 1):
            total = total + 1
            break
          
print(total)
