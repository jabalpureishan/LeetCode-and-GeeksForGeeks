class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        ans = []
        for j,i in enumerate(variables):
            if (((i[0]**i[1])%10)**i[2])%i[3]==target:
                ans.append(j)
        return ans
        