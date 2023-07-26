class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(nums,k):
            nums.append(float("inf"))
            total = count = 0
            for i in range(len(nums)):
                if nums[i]<=k:
                    count += 1
                else:
                    total += (count*(count+1))//2
                    count = 0
            return total

        return count(nums,right) - count(nums,left-1)
