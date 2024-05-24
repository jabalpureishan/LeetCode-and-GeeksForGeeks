class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r,Max = 0,len(height)-1,0
        while l<r:
            Max = max(Max,(r-l)*min(height[l],height[r]))
            if height[l]<=height[r]:
                l += 1
            else:
                r -= 1
            
        return Max
        