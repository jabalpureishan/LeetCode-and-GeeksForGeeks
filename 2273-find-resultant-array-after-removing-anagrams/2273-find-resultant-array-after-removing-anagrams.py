class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        new = set()
        first = "".join(sorted(words[0]))
        check = [first]
        out = [words[0]]
        for i in range(1,len(words)):
            pick = words[i]
            res = "".join(sorted(pick))
            if res!=check[i-1]:
                out.append(pick)
            check.append(res)
        return out
