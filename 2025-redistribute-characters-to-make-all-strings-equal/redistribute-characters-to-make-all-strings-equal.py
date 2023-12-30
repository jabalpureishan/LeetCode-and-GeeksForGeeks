class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d = {}
        for i in words:
            for j in i:
                d[j] = d.get(j,0) + 1
        n = len(words)
        for i in d:
            if d[i]%n!=0:
                return False
        return True
        