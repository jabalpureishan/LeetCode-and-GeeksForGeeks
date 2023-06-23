class Solution:
    def longestPalindrome(self, s: str) -> str:
        L =len(s)
        for i in range(L,0,-1):
            window = i
            slides = L - window + 1
            for j in range(slides):
                R = s[j:window]
                if(R==R[::-1]):
                    return(R)
                window+=1
        