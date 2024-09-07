class Solution:
    def stringHash(self, s: str, k: int) -> str:
        a = "abcdefghijklmnopqrstuvwxyz"
        d = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
        n = len(s)
        ans = ""
        for i in range(0,n,k):
            total = 0
            for j in range(i,i+k):
                total += d[s[j]]
            total %= 26
            ans += a[total]
        return ans
        