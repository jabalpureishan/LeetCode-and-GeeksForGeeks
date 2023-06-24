class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            pick = nums[i]
            if pick in n:
                return [n[pick],i]
            else:
                n[target-pick] = i
        return []