class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        Max = l = 0
        d = {0:0,1:0}
        for r in range(len(nums)):
            d[nums[r]] += 1
            while(d[0]>1):
                d[nums[l]] -= 1
                l += 1
            Max = max(Max,r-l+1)
        return Max-1