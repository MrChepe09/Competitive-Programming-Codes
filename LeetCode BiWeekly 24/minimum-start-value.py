class Solution:
  def minStartValue(self, nums: List[int]) -> int:
    start = 0
    count = 0
    for i in nums:
      start += i
      count = min(count, start)
  return max(abs(count)+1, 1)
