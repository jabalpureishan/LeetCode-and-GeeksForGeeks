class Solution:
    def removeStars(self, s: str) -> str:
        stars = s.count("*")
        while(stars>0):
            ind = s.index("*")
            s = s[:ind-1] + s[ind+1:]
            stars -= 1
        return s