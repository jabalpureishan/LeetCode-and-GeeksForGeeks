class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hashmap = {}
        for i in arr:
            hashmap[i] = hashmap.get(i,0) + 1
        hashmap = sorted(hashmap.items(),key=lambda x:x[1])
        actual = len(hashmap)
        length = len(hashmap)
        #print(hashmap)
        ind = 0
        while(k>0 and ind<actual):
            k -= hashmap[ind][1]
            if k>=0:
                length -= 1
            ind += 1
        return length