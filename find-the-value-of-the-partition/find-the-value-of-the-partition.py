class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        Min = float("inf")
        nums.sort()
        for i in range(1,len(nums)):
            Min = min(Min,nums[i]-nums[i-1])
        return Min

        