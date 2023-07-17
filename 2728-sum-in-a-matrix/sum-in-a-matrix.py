class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        new = []
        for i in nums:
            curr = sorted(i,reverse=True)
            new.append(curr)
        count = 0
        for i in range(len(nums[0])):
            Max = 0
            for j in range(len(nums)):
                Max = max(Max,new[j][i])
            count += Max
        return count