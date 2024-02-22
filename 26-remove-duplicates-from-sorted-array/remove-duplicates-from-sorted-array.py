class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ind = 1
        while ind<len(nums):
            if nums[ind]==nums[ind-1]:
                nums.pop(ind)
            else:
                ind += 1
        return ind
        