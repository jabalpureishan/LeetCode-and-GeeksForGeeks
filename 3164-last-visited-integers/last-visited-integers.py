class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = []
        seen = set()
        for i in range(len(words)):
            if words[i]=="prev":
                seen.add(i)
                for j in range(i-1,-1,-1):
                    if j not in seen and words[j]!="prev":
                        ans.append(int(words[j]))
                        seen.add(j)
                        break
                else:
                    ans.append(-1)
            else:
                seen = set()
        return ans
                        