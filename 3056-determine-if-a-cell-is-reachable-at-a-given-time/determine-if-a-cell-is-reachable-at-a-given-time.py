class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        Max = max(abs(fy-sy),abs(fx-sx))
        if Max==0:
            if t==1:
                return False
            return True
        return t>=Max
        