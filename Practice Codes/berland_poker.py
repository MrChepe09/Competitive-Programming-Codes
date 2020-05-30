def poker(n, m, k):
  card = n//k
  a1 = min(m, card)
  a2 = (m-a1+k-2)//(k-1)
  return (a1-a2)
    
      
      

test = int(input())
for i in range(test):
  n, m, k = map(int, input().split())
  print(poker(n, m, k))
