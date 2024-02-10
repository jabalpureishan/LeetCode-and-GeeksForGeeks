class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        new = word[k:]
        count = 1
        while not word.startswith(new):
            count += 1
            new = new[k:]
        return count
        