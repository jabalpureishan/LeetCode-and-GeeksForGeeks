class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        h = float("-inf")
        for i in range(n-1,-1,-1):
            h = max(h,min(citations[i],n-i))
        return h


        