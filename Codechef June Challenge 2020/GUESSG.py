def guessing(n):
  turn = 1
  low = 1
  high = n
  while(True):
    mid = (low+high)//2
    print(mid)
    ans = input()
    if(ans=='E'):
      return
    if(low==high):
      low = 1
      high = n
      turn += 1
      break
    if(turn%2==1):
      if(ans=='G'):
        low = mid+1
      else:
        high = mid-1
    turn+=1

  while(True):
    mid = (low+high)//2
    print(mid)
    ans = input()
    if(ans=='E'):
      return
    if(turn%2==0):
      if(ans=='G'):
        low = mid+1
      else:
        high = mid-1
    turn+=1


n = int(input())
guessing(n)




