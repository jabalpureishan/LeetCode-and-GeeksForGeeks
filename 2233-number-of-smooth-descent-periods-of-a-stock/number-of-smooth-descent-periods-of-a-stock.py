class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        prices.append(prices[-1]+1)
        total = 0
        count = 1
        for i in range(1,len(prices)):
            if prices[i-1]-prices[i]==1:
                count += 1
            else:
                total += (count*(count+1))//2
                count = 1
        return total