class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        D,Output={},[]
        for i in words:
            D[i] = D.get(i,0)+1
        New = {}
        for i in D:
            New[D.get(i)] = []
        for i in D:
            New.get(D.get(i)).append(i)
        New = sorted(New.items(),key = lambda x:x[0],reverse=True)
        for i in New:
            if len(Output)>k:
                break
            res = sorted(i[1])
            Output.extend(res)
        return Output[:k]