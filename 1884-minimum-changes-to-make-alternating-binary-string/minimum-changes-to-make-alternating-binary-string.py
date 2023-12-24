class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        curr = "1"
        count1 = 0
        for i in range(n):
            if s[i]!=curr:
                count1 += 1
            if curr=="0":
                curr = "1"
            else:
                curr = "0"
        count2 = 0
        curr = "0"
        for i in range(n):
            if s[i]!=curr:
                count2 += 1
            if curr=="0":
                curr = "1"
            else:
                curr = "0"
        return min(count1,count2)