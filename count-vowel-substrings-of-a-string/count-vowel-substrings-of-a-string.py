class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = {"a","e","i","o","u"}
        count = 0
        length = len(word)
        for i in range(5,length+1):
            window = i
            slides = length - window + 1
            for j in range(slides):
                if (set(word[j:window]))==vowels :
                    count += 1
                window += 1
        return count

