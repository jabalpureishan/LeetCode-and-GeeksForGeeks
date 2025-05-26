class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = Max = 0
        hmap = {0:0,1:0}
        for right in range(len(nums)):
            hmap[nums[right]] += 1
            while hmap[0]>k:
                hmap[nums[left]] -= 1
                left += 1
            Max = max(Max,hmap[0]+hmap[1])
        return Max


        