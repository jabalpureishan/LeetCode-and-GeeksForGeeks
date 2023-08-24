class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        def func(nums,k):
            nums.sort()
            left,right,count = 0,1,0
            while(right<len(nums)):
                diff = nums[right] - nums[left]
                if diff>k:
                    left += 1
                    diff = nums[right] - nums[left]
                else:
                    count += right - left
                    right += 1
            return count
        return func(nums,k) - func(nums,k-1)