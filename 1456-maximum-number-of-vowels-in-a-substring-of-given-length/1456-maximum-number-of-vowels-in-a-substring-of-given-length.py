class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        length = len(s)
        window = k
        slides = length - window 
        vowels = {"a","e","i","o","u"}
        Max = 0
        for i in range(k):
            if s[i] in vowels:
                Max += 1
        count = Max
        for j in range(slides):
            if s[window] in vowels:
                count += 1
            if s[j] in vowels:
                count -= 1
            Max = max(Max,count)
            window += 1
        return Max
        