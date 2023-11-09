from sortedcontainers import SortedList
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums = SortedList(nums)
        for i in range(k):
            temp = nums[0]
            del nums[0]
            nums.add(-temp)
        return sum(nums)
        