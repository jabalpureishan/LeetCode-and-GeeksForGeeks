from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(d, dt):
            for i in dt:
                if d[i] < dt[i]:
                    return False
            return True

        output = ""
        lens = len(s)
        lent = len(t)
        dt = Counter(t)

        min_length = float('inf')
        start = 0
        left = 0
        counter = 0

        for right in range(lens):
            if dt[s[right]] > 0:
                counter += 1
            dt[s[right]] -= 1

            while counter == lent:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                dt[s[left]] += 1
                if dt[s[left]] > 0:
                    counter -= 1
                left += 1

        if min_length == float('inf'):
            return ""
        else:
            return s[start:start + min_length]