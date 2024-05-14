class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        for i in range(1,len(nums)):
            if nums[i]!=nums[ind]:
                nums[ind+1] = nums[i]
                ind += 1
        return ind+1
        