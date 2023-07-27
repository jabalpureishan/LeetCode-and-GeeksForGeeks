class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i in d:
            if d[i]==1:
                return i