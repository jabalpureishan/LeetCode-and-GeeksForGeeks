class Solution:
    def numSteps(self, s: str) -> int:
        s,count = int(s,2),0
        while s>1:

            if s&1==0:
                s //= 2
            else:
                s += 1
            count += 1
        return count