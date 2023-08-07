class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        out = []
        for i in matrix:
            out.extend(i)
        if target in out:
            return True
        else:
            return False