class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] in d:
                d[groupSizes[i]].append(i)
            else:
                d[groupSizes[i]] = [i]
        ans = []
        for i in d:
            for j in range(0,len(d[i]),i):
                ans.append(d[i][j:j+i])
        return ans
        