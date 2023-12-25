from collections import Counter
from sortedcontainers import SortedList
class Solution:
    def minDeletions(self, s: str) -> int:
        s = Counter(s)
        s = SortedList(s.values())
        count = 0
        ind = -1
        while ind>-len(s):
            if s[ind]==s[ind-1]:
                temp = s[ind]
                del s[ind]
                if temp!=1:
                    s.add(temp-1)
                count += 1
            else:
                ind -= 1
        return count
            