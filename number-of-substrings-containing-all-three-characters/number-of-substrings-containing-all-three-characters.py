class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        right = left = count = 0
        length = len(s)
        d = {"a":0,"b":0,"c":0}
        for right in range(length):
            d[s[right]] = d.get(s[right],0) + 1
            while(d.get("a",0)>0 and d.get("b",0)>0 and d.get("c",0)>0):
                count += length - right
                d[s[left]] -= 1
                left += 1
        return count
