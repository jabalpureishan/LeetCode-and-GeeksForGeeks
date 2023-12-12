class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sMax = Max = 0
        for i in nums:
            if i>=sMax:
                Max = sMax
                sMax = i
            elif i<sMax and i>Max:
                Max = i
        return (sMax-1)*(Max-1)
        