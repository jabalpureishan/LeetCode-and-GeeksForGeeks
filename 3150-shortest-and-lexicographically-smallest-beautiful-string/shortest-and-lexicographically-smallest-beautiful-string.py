class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        one = left = 0
        length = len(s)
        Min = float("inf")
        ans = s
        for right in range(length):
            if s[right]=="1":
                one += 1
            while one>k :
                if s[left]=="1":
                    one -= 1
                left += 1
            #print(s[left:right+1])
            curr = s[left:right+1].strip("0")
            #print("curr:",curr)
            if one==k:
                lenc = len(curr)
                if lenc<Min:
                    Min = lenc
                    ans = curr
                elif lenc==Min:
                    ans = min(ans,curr)
                    
        if Min == float("inf"):
            return ""
        return ans
        