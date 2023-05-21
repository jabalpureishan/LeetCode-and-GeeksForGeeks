class Solution:
    def minLength(self, s: str) -> int:
        left = True
        while left:
            index = 0
            left = False
            length = len(s)
            while index<(length-1):
                if s[index:index+2]=="AB" or s[index:index+2]=="CD":
                    s = s[:index] + s[index+2:]
                    left = True
                else:
                    index += 1
        return len(s)
        
        