class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        curr1 = "1"
        curr2 = "0"
        count1 = count2 = 0
        for i in range(n):
            if s[i]!=curr1:
                count1 += 1
            if s[i]!=curr2:
                count2 += 1
            if curr1=="0":
                curr1 = "1"
            else:
                curr1 = "0"
            if curr2=="0":
                curr2 = "1"
            else:
                curr2 = "0"
        return min(count1,count2)