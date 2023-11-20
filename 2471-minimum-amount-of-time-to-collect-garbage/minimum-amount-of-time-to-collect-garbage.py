class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pfx = []
        sum_ = 0
        G=M=P=0
        lg=lm=lp=-1
        travel = [0]+travel
        n = len(garbage)
        for ind,val in enumerate(garbage) :
            d = Counter(val)
            # print(d)
            if "G" in d:
                lg = ind
                G += d["G"]
            if "M" in d:
                lm = ind
                M += d["M"]
            if "P" in d:
                lp = ind
                P += d["P"]
            sum_ += travel[ind]
            pfx.append(sum_)
        # print(pfx)
        # print(lg,lm,lp)
        # print(G,M,P)
        if lg!=-1:
            G += pfx[lg]
        if lm!=-1:
            M += pfx[lm]
        if lp!=-1:
            P += pfx[lp]
        
        return G+M+P