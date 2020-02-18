class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(int(len(nums))):
            g = target-nums[i] in nums
            if(g):
                r = nums.index(target-nums[i])
            if(g and i!=r):
                break
        return [i, r]
