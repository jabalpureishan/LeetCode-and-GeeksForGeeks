class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length==0:
            return length
        Max = 1
        for i in range(length):
            curr = set(s[i])
            for j in range(i+1,length):
                if s[j] not in curr:
                    curr.add(s[j])
                else:
                    break
                Max = max(Max,len(curr))
        return Max




