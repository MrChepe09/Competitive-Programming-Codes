import math
def collision(d):
  count = 0
  for i in d:
    count += (d[i]*(d[i]-1))//2
  return count


n = int(input())
d = {}
for i in range(n):
  x, y, t = map(int, input().split())
  l = math.sqrt((x**2)+(y**2))
  time = l/t
  if(time in d):
    d[time] += 1
  else:
    d[time] = 1
print(collision(d))
