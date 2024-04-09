# from sortedcontainers import SortedList
class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        med = n//2
        ans = 0
        ind = med
        for i in range(med,n):
            if  nums[i]<k:
                ans += k-nums[i]
                nums[i] =k
        for i in range(med+1):
            if nums[i]>k:
                ans += nums[i]-k
        return ans
        