def nastyarice(n, a, b, c, d):
  w1 = (a-b)*n
  w2 = (a+b)*n
  w3 = c-d
  w4 = c+d
  if(w2<w3 or w4<w1):
    return "No"
  else:
    return "Yes"

test = int(input())
for i in range(test):
  n, a, b, c, d = map(int, input().split())
  print(nastyarice(n, a, b, c, d))
