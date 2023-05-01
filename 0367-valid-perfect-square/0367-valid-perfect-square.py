class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        ans = str(sqrt(num))
        if ans[-2:]==".0":
            return True
        return False