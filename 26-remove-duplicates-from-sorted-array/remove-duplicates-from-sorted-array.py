class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        n = len(nums)
        nums.append(nums[-1]+1)
        for i in range(n):
            if nums[i]!=nums[i+1]:
                nums[ind] = nums[i]
                ind += 1
        return ind
        