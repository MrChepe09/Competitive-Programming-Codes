test = int(input())
for i in range(test):
  r0, c0 = map(int, input().split())
  steps = 25
  step = [[2, 2], [3, 1], [1, 3], [2, 2], [3, 3], [5, 1], [1, 5], [3, 3], [4, 4], [7, 1], [1, 7], [4, 4], [5, 5], [8, 2], [2, 8], [5, 5], [6, 6], [8, 4], [4, 8], [6, 6], [7, 7], [8, 6], [6, 8], [7, 7], [8, 8]]
  if(r0!=1 or c0!=1):
    steps += 2
    extra = [[int((r0+c0)/2), int((r0+c0)/2)], [1,1]]
    step = extra + step
  print(steps)
  for j in range(len(step)):
    print(step[j][0], step[j][1])
