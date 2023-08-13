class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s = "".join(sorted(s,key=lambda x:order.find(x)))
        return s