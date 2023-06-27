class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s)-1
        while(a<b):
            #print("s[a]:",s[a],"s[b]",s[b])
            if not s[a].isalnum():
                a += 1
                continue
                #print("a",a)
            if not s[b].isalnum():
                b -= 1
                continue
                #print("b",b)
            
            if s[a].lower()!=s[b].lower():
                return False
            a+=1
            b-=1
        return True