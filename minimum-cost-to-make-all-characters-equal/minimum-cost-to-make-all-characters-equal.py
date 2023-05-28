class Solution:
    def minimumCost(self, s: str) -> int:
        length = len(s)
        result = -1
        j = 0
        while(j<(length-1)):
            if s[j+1]!=s[j]:
                if (j+1)>=(length-j-1):
                    result = result + length - j - 1
                else:
                    result = result + j + 1
            j += 1
        result += 1
        return result
        
        