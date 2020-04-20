class Solution:
  def findMinFibonacciNumbers(self, k: int) -> int:
    fibo = [1, 1]
    i = 2
    count = 0
    ans = fibo[i-1] + fibo[i-2]
    while(ans<=k):
      i+=1
      fibo.append(ans)
      ans = fibo[i-1] + fibo[i-2]
    for t in range(len(fibo)-1, -1, -1):
      if(k==0):
        return count
      elif(k>=fibo[t]):
        k-=fibo[t]
        count+=1
    return count
