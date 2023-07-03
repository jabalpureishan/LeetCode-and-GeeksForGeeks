class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        length = len(s)
        set_ = set()
        Max = 0
        for right in range(length):
            #print("curr:",s[right])
            if s[right] in set_:
                #print("in set")
                while(left<right):
                    set_.discard(s[left])
                    #print("removed:",s[left],"so:",set_)
                    left += 1
                    if s[left-1]==s[right]:
                        break
            set_.add(s[right])
            #print("set:",set_)
            Max = max(Max,len(set_))
        return Max




