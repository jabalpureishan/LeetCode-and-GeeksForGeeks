class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        ans = []
        for ind,row in enumerate(rowSum):
            ans.append([])
            for i,col in enumerate(colSum):
                Min = min(rowSum[ind],colSum[i])
                ans[ind].append(Min)
                rowSum[ind] -= Min
                colSum[i] -= Min
                #print(rowSum,colSum)
        return ans

        