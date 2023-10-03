class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d,count = dict(),0
        for i in nums:
            count += d.get(i,0)
            d[i] = d.get(i,0) +1
        return count
