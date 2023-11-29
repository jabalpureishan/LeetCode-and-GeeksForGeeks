class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        length,d = len(votes[0]),{}
        for i in sorted(votes[0]):
            d[i] = [0]*length
        for i in votes:
            for j,k in enumerate(i):
                d[k][j] += 1
        d = sorted(d.items(),key=lambda x:x[1],reverse=True)
        ans = ""
        for i in d:
            ans += i[0]
        return ans
