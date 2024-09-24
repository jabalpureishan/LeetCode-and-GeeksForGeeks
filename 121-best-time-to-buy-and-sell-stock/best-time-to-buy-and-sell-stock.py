class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        arr =prices
        Max,Min = 0,arr[0]
        for i in arr:
            Min = min(Min,i)
            Max = max(Max,i-Min)
        return Max
        