class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curr,avg = 0,0
        for i in customers:
            curr = max(curr,i[0])
            curr += i[1]
            avg += curr-i[0]
        return float("{0:.5f}".format(avg/len(customers)))     