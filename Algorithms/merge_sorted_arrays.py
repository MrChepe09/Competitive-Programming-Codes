def mergesortarr(nums1, m, nums2, n):
  for i in range(n-1, -1, -1):
    last = nums1[m-1]
    j = m-2
    while(j>=0 and nums1[j]>nums2[i]):
      nums1[j+1] = nums1[j]
      j-=1
    if(j!=m-2 or last>nums2[i]):
      nums1[j+1] = nums2[i]
      nums2[i] = last
  return nums1, nums2


test = int(input())
for i in range(test):
  m = int(input())
  nums1 = list(map(int, input().split()))
  n = int(input())
  nums2 = list(map(int, input().split()))
  print(mergesortarr(nums1, m, nums2, n))
