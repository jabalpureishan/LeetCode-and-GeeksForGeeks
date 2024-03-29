class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        dec,inc = True,True
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                inc = False
            if nums[i]>nums[i-1]:
                dec = False
        return dec or inc