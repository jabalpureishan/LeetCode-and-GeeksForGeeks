class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        d = {}
        for i in paths:
            d[i[0]] = i[1]
        l = len(d)
        curr = paths[0][0]
        count = 0
        while count<l and curr in d:
            curr = d[curr]
            count += 1
        return curr