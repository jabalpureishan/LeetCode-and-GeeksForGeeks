class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        Output =[]
        for i in nums:
            Output.append(i*i)
        Output.sort()
        return Output