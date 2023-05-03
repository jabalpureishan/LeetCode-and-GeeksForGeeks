from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        P = permutations(nums,len(nums))
        output = []
        index = 0
        for i in P:
            output.append(i)
            index+=1
        output = set(output)
        return output