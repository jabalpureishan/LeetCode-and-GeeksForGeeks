class Solution:
    def largestGoodInteger(self, num: str) -> str:
        length = len(num)
        Max = ""
        for i in range(length-2):
            curr = num[i:i+3]
            if len(set(curr))==1:
                Max = max(Max,curr)
        return Max

        