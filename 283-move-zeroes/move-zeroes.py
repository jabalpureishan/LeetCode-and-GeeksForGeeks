class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        length = len(nums)
        ind = 0
        for i in range(length):
            if nums[ind]==0:
                nums.pop(ind)
                nums.append(0)
            else:
                ind += 1
        return nums
