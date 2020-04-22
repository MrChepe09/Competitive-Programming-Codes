def binary_search(a, n):
  start = 0
  end = len(a)-1
  while(start<=end):
    mid = int((start+end)/2)
    if(a[mid]==n):
      return mid
    elif(a[mid]<n):
      start = mid+1
    else:
      end = mid-1
  return -1
  


p = list(map(int, input().split()))
a = p[1:]
n = list(map(int, input().split()))
ans = []
for i in range(1, n[0]+1):
  g = binary_search(a, n[i])
  ans.append(g)
print(*ans)
