class Solution:
    def compressedString(self, word: str) -> str:
        word += "$"
        comp,count,n = "",1,len(word)
        for i in range(1,n):
            if word[i-1]==word[i]:
                count += 1
                if count==9:
                    comp += "9"+word[i]
                    count = 0
            else:
                if count!=0:
                    comp += str(count)+word[i-1]
                count = 1
        return comp

        