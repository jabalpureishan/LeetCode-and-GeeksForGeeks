class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        XOR = nums[0]
        n = len(nums)
        for i in range(1,n):
            XOR ^= nums[i]
        return XOR

        