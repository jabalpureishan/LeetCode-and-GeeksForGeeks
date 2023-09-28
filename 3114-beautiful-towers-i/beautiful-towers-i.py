class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        ans = -1
        length = len(maxHeights)
        for i in range(length):
            Sum = curr = maxHeights[i]
            for j in range(i+1,length):
                curr = min(maxHeights[j],curr)
                Sum += curr
            curr = maxHeights[i]
            for j in range(i-1,-1,-1):
                curr = min(maxHeights[j],curr)
                Sum += curr
            ans = max(Sum,ans)  
        return ans
        