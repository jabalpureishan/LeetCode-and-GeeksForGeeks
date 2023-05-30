class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            srt = "".join(sorted(i))
            if srt not in d:
                d[srt] = [i]
            else:
                d[srt].append(i)
        out = []
        for i in d.values():
            out.append(i)
        return out