class Solution:
    def countSubstrings(self, s: str) -> int:
        n,count = len(s),0
        for i in range(n):
            for j in range(i+1,n+1):
                curr = s[i:j]
                if curr==curr[::-1]:
                    count += 1
        return count
        