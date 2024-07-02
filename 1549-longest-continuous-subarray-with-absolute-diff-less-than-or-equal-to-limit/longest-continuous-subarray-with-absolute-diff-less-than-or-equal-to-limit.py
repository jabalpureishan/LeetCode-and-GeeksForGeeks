from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        Max = left = 0
        List = SortedList([])
        for right in range(len(nums)):
            List.add(nums[right])
            while List[-1]-List[0]>limit:
                List.remove(nums[left])
                left += 1
            Max = max(Max,right-left+1)
        return Max
        