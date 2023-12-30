class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        d = Counter("".join(words))
        for i in d:
            if d[i]%n!=0:
                return False
        return True