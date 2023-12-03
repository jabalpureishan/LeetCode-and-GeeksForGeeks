class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans,length = 0,len(points)
        for i in range(1,length):
            ans += max(abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return ans
        