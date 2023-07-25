class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        start = length-k
        Sum = sum(cardPoints[start:])
        #print("first:",Sum)
        Max = Sum
        #print(start,k)
        for i in range(start,length):
            #print("start:",i)
            #print("end:",(i+k)%length)
            Sum += cardPoints[(i+k)%length]
            Sum -= cardPoints[i%length]
            #print("Sum:",Sum)
            Max = max(Max,Sum)
        return Max