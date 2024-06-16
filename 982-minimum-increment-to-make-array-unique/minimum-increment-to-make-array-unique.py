class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        ans = 0
        for i in range(1,len(nums)):
        
            if nums[i]<=nums[i-1]:
                temp = nums[i]
                nums[i] = nums[i-1] + 1
                ans += nums[i]-temp

        print(nums)
        return ans        