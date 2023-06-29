class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        right = sum(nums)
        left = 0
        count = 0
        for i in range(len(nums)-1):
            left += nums[i]
            right -= nums[i]
            if left>=right:
                count += 1
        return count