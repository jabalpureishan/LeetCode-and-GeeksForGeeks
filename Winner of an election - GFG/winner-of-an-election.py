#User function Template for python3

class Solution:
    
    #Complete this function
    
    #Function to return the name of candidate that received maximum votes.
    def winner(self,arr,n):
        d = {}
        M = arr[0]
        Max = 0
        out = []
        for i in arr:
            d[i] = d.get(i,0) + 1
        D = {}
        for i in d.values():
            Max = max(Max,i)
        for i in d:
            if d.get(i)==Max:
                out.append(i)
        out.sort()
        #out.sort(key=lambda x:len(x))
        return [out[0],Max]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends