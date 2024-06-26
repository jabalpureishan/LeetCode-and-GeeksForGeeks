
class Solution:
    def trap(self, height: List[int]) -> int:
        lmax,rmax,r,l,ans = 0,0,len(height)-1,0,0
        while l<r:
            if height[l]<=height[r]:
                if height[l]>=lmax:
                    lmax = height[l]
                else:
                    ans += lmax - height[l]
                l += 1
            else:
                if height[r]>=rmax:
                    rmax = height[r]
                else:
                    ans += rmax - height[r]
                r -= 1
        return ans
            