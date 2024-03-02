class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:    
        b = [max(ax1,bx1),max(ay1,by1)]
        t = [min(ax2,bx2),min(ay2,by2)]
        return (ax2-ax1)*(ay2-ay1)+(bx2-bx1)*(by2-by1)-max(0,t[0]-b[0])*max(0,t[1]-b[1])