class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = max(nums)
        last = nums.index(n)
        first = nums.index(1)
        count = len(nums)-1-last + first
        if last<first:
            count -= 1
        return count