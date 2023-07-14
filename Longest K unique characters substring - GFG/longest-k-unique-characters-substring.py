#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        Max = -1
        j = 0
        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i],0) + 1
            while(len(d)>k and j<i):
                d[s[j]] -= 1
                
                if d[s[j]]==0:
                    d.pop(s[j])
                j += 1
            if len(d)==k:
                Max = max(Max,i-j+1)
        return Max


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends