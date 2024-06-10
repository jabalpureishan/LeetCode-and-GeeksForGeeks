class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        for i,j in enumerate(sorted(heights)):
            if j!=heights[i]:
                count += 1
        return count