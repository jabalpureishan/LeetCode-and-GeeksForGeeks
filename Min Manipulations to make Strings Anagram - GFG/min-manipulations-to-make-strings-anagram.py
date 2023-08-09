#User function Template for python3
class Solution:
    def minManipulation(self, N, S1, S2): 
        d1,d2,count = {},{},0
        for i in range(N):
            d1[S1[i]] = d1.get(S1[i],0) + 1
            d2[S2[i]] = d2.get(S2[i],0) + 1
        for i in d1:
            count += max(0,d1[i] - d2.get(i,0))
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        S1,S2 = input().strip().split()
        ob = Solution()
        ans = ob.minManipulation(N, S1, S2)
        print(ans)
# } Driver Code Ends