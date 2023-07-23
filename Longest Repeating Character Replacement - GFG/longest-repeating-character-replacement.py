#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def characterReplacement(self, S, K):
        s=S
        k=K
        Max = j = curr = 0
        d = {}
        ele = s[0]
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            if d[s[i]]>curr:
                curr = d[s[i]]
                ele = s[i]
            while(((i-j+1)-curr)>k):
                d[s[j]] -= 1
                if s[j]==ele:
                    ans = max(d.items(),key = lambda x:x[1])
                    ele = ans[0]
                    curr = ans[1]
                j += 1
            Max = max(Max,i-j+1)
        return Max

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range(t):
        S = input().strip()
        K = int(input())
        ob = Solution()
        res = ob.characterReplacement(S, K)
        print(res)
# } Driver Code Ends