from sortedcontainers import SortedDict
class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        d = SortedDict({})
        for ind,val in enumerate(s):
            if val=="*":
                s[ind] = ""
                k = None
                for k in d:
                    break
                if k!=None:
                    s[d[k][-1]] = ""
                    d[k].pop()
                    if len(d[k])==0:
                        d.pop(k)
            else:
                if val not in d:
                    d[val] = [ind]
                else:
                    d[val].append(ind)
        return "".join(s)
        