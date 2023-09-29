class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = nums[:]
        dec = nums[:]
        inc.sort()
        dec.sort(reverse=True)
        if inc==nums or dec==nums:
            return True
        return False