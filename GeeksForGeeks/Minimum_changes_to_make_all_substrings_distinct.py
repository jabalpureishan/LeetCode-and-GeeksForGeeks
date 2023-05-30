class Solution:
    def minChange(S):
        d = {}
        for i in S:
            d[i] = d.get(i,0) + 1
        out = 0
        for i in d.values():
            out += i - 1
        return out

    print(minChange("aab"))
    print(minChange("ab"))