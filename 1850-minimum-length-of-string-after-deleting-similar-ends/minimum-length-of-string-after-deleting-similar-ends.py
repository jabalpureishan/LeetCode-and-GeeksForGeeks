class Solution:
    def minimumLength(self, s: str) -> int:
        start,n = 0,len(s)
        end = n-1
        while start<end:
            if s[start]!=s[end]:
                break
            curr = s[start]

            while start<=end and s[start]==curr:
                start += 1
            while end>=start and s[end]==curr:
                end -= 1

            #print(s[start:end+1],start,end)
        return end-start+1
        