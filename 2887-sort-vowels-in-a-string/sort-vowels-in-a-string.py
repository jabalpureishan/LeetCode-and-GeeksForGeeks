class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a","e","i","o","u","A","E","I","O","U"}
        v = []
        for i in s:
            if i in vowels:
                v.append(i)
        v.sort()
        ind = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s = s[:i] + v[ind] + s[i+1:]
                ind += 1
        return s