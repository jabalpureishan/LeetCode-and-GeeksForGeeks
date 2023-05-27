class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        loop = min(l1,l2)
        output = ""
        for i in range(loop):
            output += word1[i] + word2[i]
        if loop==l1:
            output += word2[loop:]
        else:
            output += word1[loop:]
        return output 