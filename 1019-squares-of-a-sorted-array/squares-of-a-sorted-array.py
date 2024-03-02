class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i,j in enumerate(nums):
            nums[i] = j*j
        return sorted(nums)
        