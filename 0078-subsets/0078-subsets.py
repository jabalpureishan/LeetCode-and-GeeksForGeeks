from itertools import combinations 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Out = [[]]
        for i in range(1,len(nums)+1):
            p = combinations(nums,i)
            for i in p:
                Out.append(i)
        return Out