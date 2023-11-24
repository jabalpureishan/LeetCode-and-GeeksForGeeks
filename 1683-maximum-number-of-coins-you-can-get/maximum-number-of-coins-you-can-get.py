class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        start = n//3
        sum_ = 0
        for i in range(start,n,2):
            sum_ += piles[i]
        return sum_
        