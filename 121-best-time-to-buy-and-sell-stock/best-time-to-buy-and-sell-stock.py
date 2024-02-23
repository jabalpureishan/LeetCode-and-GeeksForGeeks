class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        Min,Max = prices[0],0
        n = len(prices)
        for i in range(1,n):
            if prices[i]>=Min:
                Max = max(Max,prices[i]-Min)
            Min = min(prices[i],Min)
        return Max
        