class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:
        ans = []
        ptr = 0
        length = len(words)
        while ptr<length :
            if ptr==length-1:
                ans.append(words[ptr])
            elif groups[ptr]!=groups[ptr+1]:
                ans.append(words[ptr])
            ptr += 1
        return ans
            
        