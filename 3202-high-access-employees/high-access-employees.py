class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        d,ans = defaultdict(list),[]
        for i in access_times:
            d[i[0]].append(int(i[1]))
        for i in d:
            lend = len(d[i])
            if lend>1:
                d[i].sort()
                for j in range(2,lend):
                    if d[i][j]-d[i][j-2]<100:
                        ans.append(i)
                        break
        return ans
            