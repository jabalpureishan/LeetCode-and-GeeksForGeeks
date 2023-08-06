class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        length = max(trips,key=lambda x:x[-1])[-1]+1
        output,Sum = length*[0],0
        for i in trips:
            if i[0]>capacity:
                return False
            output[i[1]-1] += i[0]
            output[i[2]-1] -= i[0]
        for i in range(length):
            Sum += output[i]
            if Sum>capacity:
                return False
        return True