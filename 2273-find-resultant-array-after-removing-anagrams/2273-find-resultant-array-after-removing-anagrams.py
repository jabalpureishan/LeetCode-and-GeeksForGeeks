class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        new = set()
        first = "".join(sorted(words[0]))
        check = [first]
        check = deque(check)
        out = [words[0]]
        for i in range(1,len(words)):
            pick = words[i]
            res = "".join(sorted(pick))
            if res!=check[0]:
                out.append(pick)
            check.append(res)
            check.popleft()
        return out
