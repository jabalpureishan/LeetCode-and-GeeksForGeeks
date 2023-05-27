class Solution:
    def addMinimum(self, word: str) -> int:
        length = len(word)
        word = "z"+word
        count = 0
        for i in range(1,length+1):
            if word[i]<=word[i-1]:
                count +=1
        #print("count:",count
        return 3*count - length