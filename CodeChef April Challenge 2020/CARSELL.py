def sellcars(n, a):
  y = 1
  for j in range(1, n):
    a[j] = max(0, a[j]-y)
    y += 1
  return sum(a)%1000000007

test = int(input())
for i in range(test):
  n = int(input())
  cars = list(map(int, input().split()))
  cars.sort(reverse=True)
  print(sellcars(n, cars))
