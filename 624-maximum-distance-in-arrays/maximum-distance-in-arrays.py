class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        Minarr,Maxarr,mn,mx = 0,0,float("inf"),float("-inf")
        for j,i in enumerate(arrays):
            if i[0]<mn:
                mn = i[0]
                Minarr = j
            if i[-1]>mx:
                mx = i[-1]
                Maxarr = j

        Max = 0
        for j,i in enumerate(arrays):
            if j!=Minarr:
                Max = max(Max,i[-1]-mn)
            if j!=Maxarr:
                Max = max(Max,mx-i[0])
        return Max       