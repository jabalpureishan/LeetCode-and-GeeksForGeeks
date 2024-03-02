class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        tr,br = topRight,bottomLeft
        n = len(bottomLeft)
        Max = 0
        for i in range(n):
            for j in range(i+1,n):
                TR = [min(tr[i][0],tr[j][0]),min(tr[i][1],tr[j][1])]
                BR = [max(br[i][0],br[j][0]),max(br[i][1],br[j][1])]
                #print(TR,BR)
                Max = max(Max,min(max(0,TR[0]-BR[0]),max(0,TR[1]-BR[1]))**2)
        return Max
            