class Solution:
    def largestGoodInteger(self, num: str) -> str:
        Max = ""
        for i in range(len(num)-2):
            curr = num[i:i+3]
            if len(set(curr))==1:
                Max = max(Max,curr)
        return Max

        