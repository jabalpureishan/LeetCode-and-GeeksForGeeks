#User function Template for python3
class Solution:
    def hashString(self, S):
        s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        d = {}
        ind = 0
        for i in s:
            d[i] = ind
            ind += 1
        S = S.split(" ")
        total = 0
        for i in S:
            for j in range(len(i)):
                total += j + d[i[j]]
        return total*len(S) 



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        print(ob.hashString(s))

# } Driver Code Ends