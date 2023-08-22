class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        length = len(s)
        window = 3
        slides = length - 2
        count = 0
        for i in range(slides):
            if len(set(s[i:window]))==3 :
                count += 1
            window += 1
        return count