class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Max,count = 0,0
        nums.append(0)
        for i in nums:
            if i==0:
                Max = max(Max,count)
                count = 0
            else:
                count += 1
        return Max
        