class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if (nums[i] < (i + 1)) and (((i + 1) < len(nums)) and (nums[i + 1] > (i + 1))):
                ans += 1
            elif (nums[i] < (i + 1)) and ((i + 1) == len(nums)):
                ans += 1
        if nums[0] > 0:
            ans += 1
        return ans
            
            
        