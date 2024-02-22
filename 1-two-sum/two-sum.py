class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for j,i in enumerate(nums):
            diff = target - i
            if diff in hmap:
                return [hmap[diff],j]
            hmap[i] = j
            