def kadane(a):
  for i in range(1, len(a)):
    a[i] = max(a[i], a[i]+a[i-1])
  return max(a)

a = list(map(int, input().split()))
print(kadane(a))
