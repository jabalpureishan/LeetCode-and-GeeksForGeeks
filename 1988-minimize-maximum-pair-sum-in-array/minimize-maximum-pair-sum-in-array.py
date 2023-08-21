class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        Max = 0
        for i in range(len(nums)//2):
            Max = max(Max,nums[i]+nums[-(i+1)])
        return Max