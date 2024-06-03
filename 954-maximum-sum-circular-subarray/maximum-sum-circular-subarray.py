class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        TSum = sum(nums)
        print(TSum)
        NMax,Sum = float("-inf"),0
        for i in nums:
            Sum += i
            NMax = max(NMax,Sum)
            Sum = max(0,Sum)
        if NMax<0:
            return NMax
        Sum,DMax = 0,float("inf")
        for i in nums:
            Sum += i
            DMax = min(Sum,DMax)
            Sum = min(0,Sum)
        print(NMax,TSum,DMax)
        return max(NMax,TSum-DMax) 
        