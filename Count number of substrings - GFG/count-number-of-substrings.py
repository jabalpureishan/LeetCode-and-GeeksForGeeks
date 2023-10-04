#User function Template for python3

class Solution:
    def substrCount (self,s, k):
        def co(s,k):
            l = count = 0
            d = {}
            for right in range(len(s)):
                d[s[right]] = d.get(s[right],0) + 1
                #print("d:",d)
                while(len(d)>k and l<=right):
                    #print("in d:",d)
                    d[s[l]] -= 1
                    if d[s[l]]==0:
                        d.pop(s[l])
                    l += 1
                count += right - l + 1 
            return count
        return co(s,k)-co(s,k-1)





#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    s = input ()
    k = int (input ())
    ob = Solution()
    print (ob.substrCount (s, k))
# } Driver Code Ends