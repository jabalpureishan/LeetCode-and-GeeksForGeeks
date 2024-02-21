class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        j,n = 0,len(nums)
        while j<n and nums[j]!=0:
            j += 1
        if j==n:
            return nums
        fr  = j+1
        for i in range(fr,n):
            #print(nums,j,i)
            if nums[i]!=0:
                nums[i],nums[j] = nums[j],nums[i]
                j += 1
            
        return nums
            