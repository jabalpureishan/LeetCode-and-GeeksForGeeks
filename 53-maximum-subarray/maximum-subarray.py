class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = float("-inf")
        sum_ = 0
        for i in nums:
            sum_ += i
            Max = max(Max,sum_)
            sum_ = max(sum_,0)
        return Max
        