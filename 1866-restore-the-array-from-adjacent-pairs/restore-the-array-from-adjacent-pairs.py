class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        freq,length,d = {},set(),{}

        def putin(d,first,sec):
            if first in d:
                d[first].append(sec)
            else:
                d[first] = [sec]
            
        for i in adjacentPairs:
            for j in i:
                freq[j] = freq.get(j,0) + 1
                length.add(j)
            putin(d,i[0],i[1])
            putin(d,i[1],i[0])
        length = len(length)
        ans = []
        for i in freq:
            if freq[i]==1:
                ans.append(i)
                break
        done = {ans[0]}
        ind = 0
        while ind<length-1:
            #print("ele:",ans[ind])
            curr = list(filter(lambda x:x not in done,d[ans[ind]]))[0]
            ans.append(curr)
            done.add(curr)
            ind += 1

        return ans

        