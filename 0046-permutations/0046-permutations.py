from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        P = permutations(nums)
        output = []
        index = 0
        for i in P:
            output.append(i)
            index+=1
        return output