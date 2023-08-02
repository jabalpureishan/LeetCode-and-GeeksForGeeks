class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = {}
        for i in words:
            curr = "".join(sorted(set(i)))
            d[curr] = d.get(curr,0) + 1
        total = 0
        #print(d)
        for i in d.values():
            i -=1 
            total += (i*(i+1))//2
        return total