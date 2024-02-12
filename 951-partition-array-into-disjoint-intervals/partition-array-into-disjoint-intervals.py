from sortedcontainers import SortedList
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        new = SortedList(nums[:])
        lMax,rMin = -1,new[0]
        for ind,ele in enumerate(nums):
            lMax = max(lMax,ele)
            new.remove(ele)
            if lMax<=new[0]:
                return ind+1
        