class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        while numBottles>0:
            if numExchange<=numBottles:
                ans += numExchange
                numBottles -= numExchange
                numBottles += 1
                numExchange += 1
            else:
                ans += numBottles
                break
        return ans
        