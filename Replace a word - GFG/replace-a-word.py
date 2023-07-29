#User function Template for python3
class Solution:
    def replaceAll (ob, S, oldW, newW):
        S = S.split(oldW)
        ans = S[0]
        for i in range(1,len(S)):
            ans += newW
            ans += S[i]
        #ans +=  S[-1]
        return ans 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S = input()
        oldW = input()
        newW = input()
        
        ob = Solution()
        print(ob.replaceAll(S, oldW, newW))
# } Driver Code Ends