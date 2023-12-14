class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def issubsequence(a,b):
            lena,lenb = len(a),len(b)
            pa = pb = 0
            while pa<lena and pb<lenb:
                if a[pa]==b[pb]:
                    pb += 1
                pa += 1
            return pb!=lenb
        ans = []
        q,p = [],[]
        for k,i in enumerate(queries):
            i += "Z"
            curr = ""
            q.append([])
            for j in i:
                if j.isupper() and curr!="":
                    if pattern[0].isupper():
                        if curr[0].isupper():
                            q[k].append(curr)
                    else:
                        q[k].append(curr)
                    curr = ""
                curr += j
        pattern+="Z"
        curr = ""
        for i in pattern:
            if i.isupper() and curr!="":
                p.append(curr)
                curr = ""
            curr += i
        lenp = len(p)
        for i in q:
                if len(i)==lenp:
                    for j in range(lenp):
                        if issubsequence(i[j],p[j]):
                            ans.append(False)
                            break
                    else:
                        ans.append(True)
                else:
                    ans.append(False)
        return ans


        