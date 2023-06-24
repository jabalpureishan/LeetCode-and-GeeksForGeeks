from sortedcontainers import SortedList
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        half = sum(nums)/2
        nums = SortedList(nums)
        count,current = 0,0
        while(current<half):
            current += nums[-1]/2
            count += 1
            nums.add(nums[-1]/2)
            nums.discard(nums[-1])
        return count  