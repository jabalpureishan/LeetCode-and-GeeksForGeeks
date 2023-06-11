class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        Max = max(nums)
        Min = min(nums)
        for i in nums:
            if i!=Max:
                if i!=Min:
                    return i
        return -1
        