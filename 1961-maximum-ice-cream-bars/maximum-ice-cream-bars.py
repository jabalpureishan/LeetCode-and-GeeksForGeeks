class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ind,n = 0,len(costs)
        while ind<n and coins>=costs[ind]:
            coins -= costs[ind]
            ind += 1
        return ind
        