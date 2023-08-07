#User function Template for python3

class Solution:

    #Function to perform case-specific sorting of strings.
    def caseSort(self,s,n):
        up,low,ans = "","",""
        for i in s:
            if i.islower():
                low += i
            else:
                up += i
        #print(up,low)
        up,low,uind,lind = sorted(up),sorted(low),0,0
        for i in s:
            if i.islower():
                ans += low[lind]
                lind += 1
            else:
                ans += up[uind]
                uind += 1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        n=int(input())
        s=str(input())
        print(Solution().caseSort(s,n))
# } Driver Code Ends