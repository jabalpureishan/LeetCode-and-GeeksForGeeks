class Solution:
    def minimumPushes(self, word: str) -> int:
        word,ans,cross,mult = Counter(word),0,7,1
        word = sorted(word.items(),key=lambda x:x[1],reverse=True)
        for i,j in enumerate(word):
            ans += j[1]*mult
            if i>=cross:
                cross += 8
                mult += 1
        return ans
        