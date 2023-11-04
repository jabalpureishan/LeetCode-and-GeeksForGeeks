class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        left.append(0)
        right.append(n)
        return max(max(left),n-min(right))
        