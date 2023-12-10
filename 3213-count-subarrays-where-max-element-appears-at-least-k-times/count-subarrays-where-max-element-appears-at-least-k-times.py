class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        Max,n = max(nums),len(nums)
        left = count = ans = 0
        for right in range(n):
            if nums[right]==Max:
                count += 1
            while left<right and count>=k:
                if nums[left]==Max:
                    count -= 1
                left += 1
            if count<k:
                ans += right - left + 1
        n = (n*(n+1))//2
        return n-ans