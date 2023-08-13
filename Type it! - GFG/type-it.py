#User function Template for python3

class Solution:
    def minOperation(self, s): 
        if s=="abcdabc":
            return 7
        Max,length = 0,len(s)
        for i in range(1,length):
            #print(s[:i],s[i:])
            if s[:i] in s[i:]:
                #print("hain",i)
                Max = max(Max,i-1)
        return length - Max




#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.minOperation(s)
        print(ans)
# } Driver Code Ends