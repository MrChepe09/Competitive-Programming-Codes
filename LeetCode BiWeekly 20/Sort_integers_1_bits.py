arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = []
for n in arr:
  count = 0
  while n > 0:
    count = count + 1
    n = n & (n-1)
  ans.append(count)
Z = [x for _,x in sorted(zip(ans,arr))]
print(Z)
