class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        Max = j = 0
        d = {1:0,0:0}
        for i in range(len(nums)):
            d[nums[i]] += 1
            while(d[0]>k):
                d[nums[j]] -= 1
                j += 1
            Max = max(Max,d[0]+d[1])
        return Max