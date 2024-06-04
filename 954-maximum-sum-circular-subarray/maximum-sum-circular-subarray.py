class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        def Maximum_Sum_Subarray(nums):
            Sum,Max = 0,float("-inf")
            for i in nums:
                Sum += i
                Max = max(Max,Sum)
                Sum = max(Sum,0)
            return Max

        def Minimum_Sum_Subarray(nums):
            Sum,Min  = 0,float("inf")
            for i in nums:
                Sum += i
                Min = min(Min,Sum)
                Sum = min(Sum,0)
            return Min

        KDN = Maximum_Sum_Subarray(nums)
        if KDN<0:
            return KDN
        return max(KDN,sum(nums) - Minimum_Sum_Subarray(nums))
        