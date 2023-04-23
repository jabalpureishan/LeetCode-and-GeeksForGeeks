class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new = []
        for i in matrix:
            new.extend(i)
        new.sort()
        return new[k-1]
        