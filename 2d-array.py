arr = []
maxi = -1000
for _ in range(6):
  arr.append(list(map(int, input().rstrip().split())))
for i in range(0, 4):
  for j in range(1, 5):
    total = arr[i][j]+arr[i][j-1]+arr[i][j+1]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j-1]+arr[i+2][j+1]
    maxi = max(maxi, total)
print(maxi)
