class Solution:
    def largestGoodInteger(self, num: str) -> str:
        length = len(num)
        Max = ""
        for i in range(length-2):
            curr = num[i:i+3]
            if curr[0]==curr[1]==curr[2]:
                Max = max(Max,curr)
        return Max

        