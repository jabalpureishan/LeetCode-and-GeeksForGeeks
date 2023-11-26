class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        v = {"a","e","i","o","u"}
        ans = 0
        lens = len(s)
        for i in range(2,lens+1,2):
            window = i
            slides = lens - window
            count = 0
            for j in s[:window]:
                if j in v:
                    count += 1
            if count==(i//2) and (count*count)%k==0:
                ans += 1
            for j in range(slides):
                if s[window] in v:
                    count += 1
                if s[j] in v:
                    count -= 1
                window += 1
                if count==(i//2) and (count*count)%k==0:
                    ans += 1
        return ans
        