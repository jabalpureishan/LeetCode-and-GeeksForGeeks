from sortedcontainers import SortedList
class Solution:
    def trap(self, height: List[int]) -> int:
        LMax = 0
        n = len(height)
        RMax = SortedList(height)
        total = 0
        for i in height:
            RMax.remove(i)
            if len(RMax)>0:
                total += max(0,min(RMax[-1],LMax) - i)
            LMax = max(LMax,i)
        return total
            