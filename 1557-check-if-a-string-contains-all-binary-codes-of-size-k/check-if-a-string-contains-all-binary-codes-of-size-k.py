class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        set_ = set()
        to = 2**k
        fr = 0
        for i in range(fr,to):
            set_.add(int(bin(i)[2:]))
        #print(set_)
        n = len(s)
        slides = n-k+1
        window = k
        for j in range(slides):
            curr = int(s[j:window])
            set_.discard(curr)
            if len(set_)==0:
                return True
            window += 1
        return False
        