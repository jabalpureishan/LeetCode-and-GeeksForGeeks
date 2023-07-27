class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        length = len(nums)
        if length==1:
            return nums[0]
        for i in range(1,length,2):
            if nums[i]!=nums[i-1]:
                return nums[i-1]
        if nums[-1]!=nums[-2]:
            return nums[-1]