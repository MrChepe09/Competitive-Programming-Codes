def knapsack(a):
  



n, w = map(int, input().split())
a = [0]*n
for i in range(n):
  p, q = map(int, input().split())
  a[i] = int(p/q)
print(knapsack(n, a))
