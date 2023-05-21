class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        output = ""
        length = len(s)
        for i in range(int(length/2)):
            first = s[i]
            second = s[-(i+1)]
            if first!=second:
                output += min(first,second)
            else:
                output+=first
        if length%2==0:
            output += output[::-1]
        else:
            output += s[(length-1)//2] + output[::-1]
        return output
        