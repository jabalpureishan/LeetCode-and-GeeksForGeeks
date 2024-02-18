class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        d = Counter(s)
        Max = max(d.values())
        set_ = set()
        for i in d:
            if d[i]==Max:
                set_.add(i)
        ans = ""
        done = set()
        for i in s[::-1]:
            if i in set_ and i not in done:
                ans += i
                done.add(i)
        return ans[::-1]

        