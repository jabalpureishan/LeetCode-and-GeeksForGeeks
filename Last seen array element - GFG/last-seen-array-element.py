#User function Template for python3

class Solution:
      
    def firstNonRepeating(self, arr, n): 
        hashmap = {}
        for i in range(n):
            if arr[i] in hashmap:
                hashmap[arr[i]].append(i)
            else:
                hashmap[arr[i]] = [i]
        return min(hashmap,key=lambda x:hashmap[x][-1])




#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import defaultdict 
            
for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))
    

# } Driver Code Ends