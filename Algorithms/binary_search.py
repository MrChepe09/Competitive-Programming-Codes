def binarySearch(a, l, r, k):
  while(l<=r):
    mid = l+(r-l)//2
    if(a[mid] == k):
      return mid
    elif(a[mid]>k):
      r = mid - 1
    else:
      l = mid + 1
  return -1

test = int(input())
for i in range(test):
  n = int(input())
  a = list(map(int, input().split()))
  k = int(input())
  print(binarySearch(a, 0, len(a)-1, k))
