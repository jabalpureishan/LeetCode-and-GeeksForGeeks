class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        length = len(s)
        def count(ged):
            ans = 0
            for i in range(len(ged)-1):
                if ged[i]==ged[i+1]:
                    ans += 1
            return ans<=1


        for i in range(length,1,-1):
            window = i
            slides = length - window + 1
            for j in range(slides):
                if count(s[j:window]):
                    return window - j
                window += 1
        return 1