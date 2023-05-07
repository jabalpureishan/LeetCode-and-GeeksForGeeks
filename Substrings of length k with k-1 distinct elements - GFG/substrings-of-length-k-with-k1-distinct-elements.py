#User function Template for python3

class Solution:
    def countOfSubstrings(self, S, K):
        d = {}
        for i in S[:K]:
            d[i] = d.get(i,0) + 1
        
        #print("first d:",d)
        count = 0
        window  = K
        slides = len(S) - window
        if len(d)==(K-1):
            count+=1
        for j in range(slides):
            Add = S[window]
            Sub = S[j]
            #print("Add:",Add,"Subtract:",Sub)
            d[Add] = d.get(Add,0) + 1
            d[Sub] -= 1
            #print("D before:",d)
            
            if d.get(Sub)==0:
                d.pop(Sub)
            if len(d)==(K-1):
                #print("count++")
                count += 1
            #print("d after:",d)
            window += 1
        return count
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        S=input()
        K=int(input())
        
        ob = Solution()
        print(ob.countOfSubstrings(S,K))
# } Driver Code Ends