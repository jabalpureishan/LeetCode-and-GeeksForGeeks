class Solution:
    def hammingWeight(self, n: int) -> int:
        x=bin(n)
        count = 0
        for i in x:
            if i=="1" :
                count += 1
        return count