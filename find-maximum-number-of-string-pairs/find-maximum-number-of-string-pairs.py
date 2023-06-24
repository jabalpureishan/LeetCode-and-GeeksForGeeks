class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pairs = 0
        word = set()
        for i in words:
            if i in word:
                pairs += 1
            word.add(i[::-1])
        return pairs
                
        