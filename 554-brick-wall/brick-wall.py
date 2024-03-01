class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        lines = sum(wall[0])-1
        hmap = {}
        Max = float("-inf")
        for i in wall:
            sum_ = 0
            n =len(i)
            for j in range(n-1):
                sum_ += i[j]
                hmap[sum_] = hmap.get(sum_,0) + 1
                Max = max(Max,hmap[sum_])
        if Max==float("-inf"):
            return len(wall)
        return len(wall)-Max
        