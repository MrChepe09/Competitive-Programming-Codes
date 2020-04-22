def lift(a):
  floor = 0
  count = 0
  for i, j in a:
    count += (abs(i-floor) + abs(j-i))
    floor = j
  return count

test = int(input())
for i in range(test):
  n, q = map(int, input().split())
  a = []
  for j in range(q):
    l = list(map(int, input().split()))
    a.append(l)
  print(lift(a))
