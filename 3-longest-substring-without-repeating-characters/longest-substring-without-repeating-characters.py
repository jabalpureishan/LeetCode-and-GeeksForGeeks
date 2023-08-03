class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left,Max,set_ = 0,0,set()
        for right in range(len(s)):
            while(s[right] in set_):
                set_.discard(s[left])
                left += 1
            set_.add(s[right])
            Max = max(Max,len(set_))
        return Max




