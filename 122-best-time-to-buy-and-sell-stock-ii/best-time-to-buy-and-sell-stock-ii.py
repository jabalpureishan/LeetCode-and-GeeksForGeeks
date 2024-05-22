class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans,Max,Min = 0,prices[0],prices[0]
        prices.append(prices[-1]-1)
        for i in range(1,len(prices)):
            if prices[i]<prices[i-1]:
                ans += Max-Min
                Max = Min = prices[i]
            Max = max(Max,prices[i])
            Min = min(Min,prices[i])
        return ans
        