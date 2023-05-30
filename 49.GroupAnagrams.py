class Solution:
    def group(strs):
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

    print(group(["eat","tea","tan","ate","nat","bat"]))
    print(group([""]))
    print(group(["a"]))
