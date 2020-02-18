test = int(input())
for i in range(test):
  n = int(input())
  st = input()
  count = st.count('1')
  ans = 0
  for j in range(count, 0, -1):
    ans += j
  print(ans)
