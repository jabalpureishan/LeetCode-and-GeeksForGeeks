class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one = left = 0
        length = len(s)
        Min = float("inf")
        ans = s
        for right in range(length):
            if s[right]=="1":
                one += 1
            while (one>k or s[left]!="1") and left<right:
                if s[left]=="1":
                    one -= 1
                left += 1
            if one==k:
                curr = right - left + 1
                if curr==Min:
                    ans = min(ans,s[left:right+1])
                elif curr<Min:
                    Min = curr
                    ans = s[left:right+1]
                    
        if Min == float("inf"):
            return ""
        return ans
        