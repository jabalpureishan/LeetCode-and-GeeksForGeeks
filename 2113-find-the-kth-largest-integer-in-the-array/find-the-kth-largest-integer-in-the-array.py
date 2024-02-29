from heapq import heappop,heapify
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        for i,j in enumerate(nums):
            nums[i] = -int(j)
        heapify(nums)
        for i in range(k-1):
            heappop(nums)
        return str(-heappop(nums))

        