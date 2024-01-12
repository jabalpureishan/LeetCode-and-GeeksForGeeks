class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count1 = count2 = 0
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)
        half = n//2
        for i in range(n):
            if s[i] in vowels:
                if i<half:
                    count1 += 1
                else:
                    count2 += 1
        return count1==count2
        