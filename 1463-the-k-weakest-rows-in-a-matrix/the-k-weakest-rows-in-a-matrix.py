class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        d = {}
        for i in range(len(mat)):
            d[i] = mat[i]
        d = sorted(d.items(),key=lambda x:x[1].count(1))
        ans = []
        for i in range(k):
            ans.append(d[i][0])
        return ans