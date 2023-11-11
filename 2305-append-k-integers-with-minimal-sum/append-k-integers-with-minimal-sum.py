class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        nums = sorted(set(nums))
        sum_ = (k*(k+1))//2
        for i in nums:
            if i in range(1,k+1):
                sum_ = sum_ +k+1-i
                k += 1
        return sum_

            