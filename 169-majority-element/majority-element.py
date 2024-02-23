class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hmap = Counter(nums)
        n = len(nums)
        for i in hmap:
            if hmap[i]>=(n/2):
                return i
        return None