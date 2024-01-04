class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set_ = set()
        to = 2**k
        fr = 0
        for i in range(fr,to):
            now = bin(i)[2:]
            now = "0"*(k-len(now))+now
            set_.add(now)
        #print(set_)
        n = len(s)
        slides = n-k+1
        window = k
        for j in range(slides):
            curr = s[j:window]
            set_.discard(curr)
            if len(set_)==0:
                return True
            window += 1
        return False
        