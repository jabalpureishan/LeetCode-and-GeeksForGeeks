class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        nums.append(nums[-1]+1)
        count,curr = 0,nums[0]
        for i in nums:
            if i==curr:
                count += 1
            else:
                if count>=(n/2):
                    return curr
                curr = i
                count = 1