class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        output = ""
        for i in s:
            output = output + i[::-1]
            output = output + " "
        return output[:-1]