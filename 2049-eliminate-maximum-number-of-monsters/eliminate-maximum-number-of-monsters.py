class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time,length,ind= [],len(dist),0
        for i in range(length):
            time.append(ceil(dist[i]/speed[i]))
        time.sort()
        for j in range(length):
            if ind>=time[j]:
                return ind
            ind += 1
        return length
        