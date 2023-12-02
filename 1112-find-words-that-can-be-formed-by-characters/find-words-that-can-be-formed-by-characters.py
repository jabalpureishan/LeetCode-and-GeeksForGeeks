class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars,ans = Counter(chars),0
        for i in words:
            curr = Counter(i)
            for j in curr:
                if curr[j]>chars.get(j,0):
                    break
            else:
                ans += len(i)
        return ans
        