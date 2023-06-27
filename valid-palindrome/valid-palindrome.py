class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s)-1
        while(a<b):
            curra = s[a]
            currb = s[b]
            chra = ord(curra)
            chrb = ord(currb)
            if chra not in range(65,91):
                if chra not in range(97,123):
                     if chra not in range(48,58):
                        a += 1
                        continue
            else:
                curra = chr(chra+32)
            if chrb not in range(65,91):
                if chrb not in range(97,123):
                    if chrb not in range(48,58):
                        b -= 1
                        continue
            else:
                currb = chr(chrb+32)
            if curra!=currb:
                return False
            a+=1
            b-=1
        return True