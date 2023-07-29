class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        d = set(dictionary)
        s = sentence.split(" ")
        for i in range(len(s)):
            curr = ""
            for j in s[i]:
                curr += j
                if curr in d:
                    s[i] = curr
                    break
        s = " ".join(s)
        return s