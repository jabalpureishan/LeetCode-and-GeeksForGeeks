#User function Template for python3
from collections import defaultdict
class Solution:

    def longestSubstrDistinctChars(self, S):
        Max = 1
        left = 0
        d = defaultdict(int)       
        for right in range(len(S)):
            d[S[right]] += 1
            while max(d.values())>1:
                d[S[left]] -= 1
                left += 1
            Max = max(Max,right-left+1)
        return Max

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends