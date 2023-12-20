class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        copy = money
        prices.sort()
        for i in range(2):
            money -= prices[i]
        if money<0:
            return copy
        return money
        
        