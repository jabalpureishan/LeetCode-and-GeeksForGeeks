class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def count(nums,k):
            if k<0:
                return 0
            left,total,Sum = 0,0,0
            for right in range(len(nums)):
                Sum += nums[right]
                while(Sum>k):
                    Sum -= nums[left]
                    left += 1
                total += right - left + 1
            return total
        return count(nums,goal) - count(nums,goal-1)