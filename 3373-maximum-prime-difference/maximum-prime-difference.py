class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prime = (False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, True, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, True)
        Min,Max = 0,n-1
        while not prime[nums[Min]] and Min<n:
            Min += 1
        while not prime[nums[Max]] and Max>0:
            Max -= 1
        return Max - Min
        