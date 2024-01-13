class Solution:
    def minSteps(self, s: str, t: str) -> int:
        ds,dt,count = {},{},0
        for i in s:
            ds[i] = ds.get(i,0) + 1
        for j in t:
            dt[j] = dt.get(j,0) + 1
        for i in ds:
            count += max(0,ds[i] - dt.get(i,0))
        return count
    