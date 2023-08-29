class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cost,ind = 0,0
        for i in customers:
            if i=="Y":
                cost += 1
        Min = cost
        for i in range(len(customers)):
            if customers[i]=="Y":
                cost -= 1
            else:
                cost += 1
            if cost<Min:
                Min = cost
                ind = i+1
        return ind