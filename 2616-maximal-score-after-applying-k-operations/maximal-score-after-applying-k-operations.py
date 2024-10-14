class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for ind,val in enumerate(nums):
            nums[ind] = -val
        heapify(nums)
        ans = 0
        for i in range(k):
            curr = heappop(nums)
            ans += -curr
            heappush(nums,floor(curr/3))
        return ans
        