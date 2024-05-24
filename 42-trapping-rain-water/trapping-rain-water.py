
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax,r,l,ans = 0,0,len(height)-1,0,0
        while l<r:
            if height[l]<=height[r]:
                ans += max(0,lmax - height[l])
                lmax = max(lmax,height[l])
                l += 1
            else:
                ans += max(0,rmax - height[r])
                rmax = max(rmax,height[r])
                r -= 1
        return ans
            