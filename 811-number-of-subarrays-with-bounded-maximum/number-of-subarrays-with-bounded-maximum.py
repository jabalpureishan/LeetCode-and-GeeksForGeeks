class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(nums,k):
            ans = l = 0
            nums.append(nums[-1]+k)
            for i in nums:
                if i>k:
                    ans += (l*(l+1))//2
                    l = 0
                else:
                    l += 1
            return ans

        return count(nums,right)-count(nums,left-1)
        