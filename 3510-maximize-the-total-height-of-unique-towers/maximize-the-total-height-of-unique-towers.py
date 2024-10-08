class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        mh,count = maximumHeight,0
        mh.sort(reverse=True)
        last = mh[0]
        for i in mh:
            if last==0: return -1
            last = min(last,i)
            count += last
            last -= 1
        return count
        