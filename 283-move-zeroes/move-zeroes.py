class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        ind = 0 
        for i in nums:
            if i==0:
                count += 1
            else:
                nums[ind] = i
                ind += 1
        if count>0:nums[-count:] = [0]*count

                    