class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        wins,loss =  set(),{}
        for i in matches:
            wins.add(i[0])
        for i in matches:
            wins.discard(i[1])
            loss[i[1]] = loss.get(i[1],0)+1
        l = []
        for i in loss:
            if loss[i]==1:
                l.append(i)
        return [sorted(wins),sorted(l)]