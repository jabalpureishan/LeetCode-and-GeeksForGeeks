class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        window = length-k
        #print("window:",window)
        Sum = sum(cardPoints[:window])
        #print("sum:",Sum)
        Min = Sum
        for i in range(length-window):
            Sum += cardPoints[window]
            Sum -= cardPoints[i]
            #print("sum:",Sum)
            #print("curr:",cardPoints[i+1:window+1])
            window += 1
            Min = min(Min,Sum)
        #print("Min:",Min)
        return sum(cardPoints) - Min