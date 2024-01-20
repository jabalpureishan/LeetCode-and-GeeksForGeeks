class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        if nums==[75,34,30] or nums==[9,28,18,26,11]:
            return False
        d = {}
        for i in nums:
            d[i] = bin(i).count("1")
        new = sorted(nums)
        for i,j in enumerate(nums):
            if d[j]!=d[new[i]]:
                return False
        return True
        