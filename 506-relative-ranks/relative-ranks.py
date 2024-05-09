class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d,ans = {},[]
        for i,j in enumerate(sorted(score,reverse=True)):
            if i==0:
                d[j] = "Gold Medal"
            elif i==1:
                d[j] = "Silver Medal"
            elif i==2:
                d[j] = "Bronze Medal"
            else:
                d[j] = str(i+1)
        for i in score:
            ans.append(d[i])
        return ans

        