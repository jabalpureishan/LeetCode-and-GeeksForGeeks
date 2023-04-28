class Solution:
    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            n = str(bin(i))
            out.append(n.count("1"))
        return out
        