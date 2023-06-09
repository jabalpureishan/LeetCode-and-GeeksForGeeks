class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        #first = letters[0]
        #letters.sort(key = lambda x:len(x))
        for i in letters:
            if i>target:
                return i
        return letters[0]