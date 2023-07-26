class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def count(nums,k,n):
            left = total = odd = 0
            for right in range(n):
                if nums[right]%2!=0:
                    odd += 1
                while(odd>k):
                    if nums[left]%2!=0:
                        odd -= 1
                    left += 1
                total += right - left + 1
            return total
        n = len(nums)
        return count(nums,k,n) - count(nums,k-1,n)