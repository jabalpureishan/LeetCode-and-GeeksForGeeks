class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        ans,n = 0,len(nums)
        for i in nums:
            ans += abs(i-nums[n//2])
        return ans