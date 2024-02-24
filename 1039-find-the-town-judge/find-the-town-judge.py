class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        d = {}
        set_ = set(range(1,n+1))
        for i in trust:
            d[i[1]] = d.get(i[1],0) + 1
            set_.discard(i[0])
        ans = -1
        for i in set_:
            ans = i
            break
        if d.get(ans,0)<(n-1):
            return -1
        return ans
        