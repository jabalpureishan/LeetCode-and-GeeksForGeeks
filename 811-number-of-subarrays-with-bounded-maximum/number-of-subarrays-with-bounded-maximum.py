from sortedcontainers import SortedList
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def totalSubarrays(nums, n, k):
            ans = 0
            i = 0
            while (i < n):
                if (nums[i] > k):
                    i += 1
                    continue
                count = 0
                while (i < n and nums[i] <= k):
                    i += 1
                    count += 1
                ans += ((count * (count + 1)) // 2)
            return ans
        length = len(nums)
        return totalSubarrays(nums,length,right) - totalSubarrays(nums,length,left-1)
