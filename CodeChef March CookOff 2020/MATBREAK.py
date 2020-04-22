def matrix_br(n, a):
  arr = [a]
  for i in range(n-1):
    a = a**a
    arr.append(a)
  ans = 0
  c = 1
  for j in arr:
    ans+=j**c
    c+=2
  return ans%1000000007

test = int(input())
for i in range(test):
  n, a = map(int, input().split())
  print(matrix_br(n, a))
