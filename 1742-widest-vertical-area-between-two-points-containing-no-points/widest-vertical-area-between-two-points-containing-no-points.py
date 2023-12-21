class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        Max = float("-inf")
        for i in range(1,len(points)):
            Max = max(Max,points[i][0]-points[i-1][0])
        return Max
        