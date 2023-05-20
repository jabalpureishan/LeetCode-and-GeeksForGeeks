class Solution:
    def maxPower(self, s: str) -> int:
        chalu = s[0]
        s += "$"
        count = 0
        Max = 0
        for i in s:
            if i==chalu:
                count += 1
            else:
                Max = max(Max,count)
                chalu = i
                count = 1
        return Max
