class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        arrays.sort(key = lambda x:x[-1])
        Max = 0
        for i in arrays[:-1]:
            Max = max(Max,arrays[-1][-1]-i[0])
        arrays.sort(key = lambda x:x[0])
        #print(arrays)
        for i in arrays[1:]:
            #print(i,arrays[0][0],i[-1])
            Max = max(Max,i[-1]-arrays[0][0])
        return Max       