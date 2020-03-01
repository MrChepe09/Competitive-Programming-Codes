test = int(input())
for i in range(test):
  a, b = map(int, input().split())
  coins = list(input().split())
  heads = coins.count('H')
  tails = coins.count('T')
  change = 0
  for j in range(a-1, a-(b+1), -1): # 4 3 
    if(coins[j]=='H' and change == 0):
      heads -= 1
      change = 1
      heads, tails = tails, heads
    elif(coins[j] == 'T' and change==0):
      tails -= 1
    elif(coins[j] == 'H' and change==1):
      tails -= 1
    elif(coins[j]=='T' and change==1):
      change = 0
      heads -= 1
      heads, tails = tails, heads
  print(heads)
    
      
