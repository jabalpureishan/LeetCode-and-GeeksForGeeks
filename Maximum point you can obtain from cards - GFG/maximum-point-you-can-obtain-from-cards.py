#{ 
 # Driver Code Starts
#Initial Template for Python 3



# } Driver Code Ends
#User function Template for python3

class Solution:
    def maxScore(self, cardPoints, N, k):
        length = len(cardPoints)
        start = length-k
        Sum = sum(cardPoints[start:])
        Max = Sum
        for i in range(start,length):
            Sum += cardPoints[(i+k)%length]
            Sum -= cardPoints[i%length]
            Max = max(Max,Sum)
        return Max

#{ 
 # Driver Code Starts.


if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N, k = map(int, input().split())
        cardPoints = list(map(int, input().split()))
        ob = Solution()
        res = ob.maxScore(cardPoints, N, k)
        print(res)
# } Driver Code Ends