class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        n = len(word)
        Max = 0
        for i in range(0,n,k):
            d[word[i:i+k]] += 1
            Max = max(Max,d[word[i:i+k]])
        return (n-Max*k)//k