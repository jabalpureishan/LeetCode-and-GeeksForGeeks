class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        d,left,Max,n = {0:0,1:0},0,0,len(nums)
        for right in range(n):
            d[nums[right]] += 1
            while d[0]>k:
                d[nums[left]] -= 1
                left += 1
            Max = max(Max,right-left+1)
        return Max