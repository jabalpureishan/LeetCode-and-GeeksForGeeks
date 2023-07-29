#User function Template for python3
class Solution:
    def replaceAll (ob, S, oldW, newW):
        newl = len(newW)
        length = len(S)
        ind = 0
        window = len(oldW)
        #print("kya?")
        while(ind<length):
            #print(S[ind:ind+window])
            if S[ind:ind+window]==oldW:
                #print("equal")
                S = S[:ind] + newW + S[ind+window:]
                ind += newl
                length += newl
                #print("new ind:",ind)
                #print("new S:",S)
            else:
                ind += 1
        return S


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