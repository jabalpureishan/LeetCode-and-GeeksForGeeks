from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
        d = Counter(arr)
        ans = list(filter(lambda x:d[x]>1,d.keys()))
        if len(ans)==0:
            return [-1]
        return sorted(ans)
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends