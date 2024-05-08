class Solution:
    def minAnagramLength(self, s: str) -> int:
        def divisors(n):
            ans = []
            i = 1
            while i*i<=n:
                if n%i==0:
                    ans.append(i)
                i += 1
            while i>0:
                if n%i==0 and n//i!=i:
                    ans.append(n//i)
                i -= 1
            return ans
        n = len(s)
        windows = divisors(n)
        for window in windows:
            curr = Counter(s[:window])
            for i in range(window,n,window):
                if Counter(s[i:i+window])!=curr:
                    break
            else:
                return window
        return n