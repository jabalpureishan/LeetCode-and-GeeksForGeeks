class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        lMax,rMin = -1,min(nums)
        for ind,ele in enumerate(nums):
            lMax = max(lMax,ele)
            if rMin==ele:
                rMin = min(nums[ind+1:])
            if lMax<=rMin:
                return ind+1
        