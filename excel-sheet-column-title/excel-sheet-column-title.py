class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while(columnNumber>26):
            div = columnNumber%26
            if div==0:
                curr = "Z"
            else:
                curr = chr(64+columnNumber%26)
            s += curr
            if div==0:
                columnNumber = columnNumber//26 - 1
            else:
                columnNumber = columnNumber//26
        s += chr(64+columnNumber)
        return s[::-1]
