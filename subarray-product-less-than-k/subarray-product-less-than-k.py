class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = 0
        prod = 1
        count = 0
        for right in range(length):
            prod *= nums[right]
            while(prod>=k and left<right):
                prod  = prod//nums[left]
                left += 1
            if prod<k:
                    count += right - left + 1
        return count