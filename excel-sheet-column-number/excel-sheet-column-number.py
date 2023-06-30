class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = columnTitle
        power = 0
        s = s[::-1]
        final = 0
        for i in s:
            final += (ord(i)-64)*(26**(power))
            power += 1
        return final
