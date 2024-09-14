class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = ind = 0
        n = len(nums)
        if n==1: return n
        for i in range(1,n):
            if nums[i]!=nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        return ind+1
  
        