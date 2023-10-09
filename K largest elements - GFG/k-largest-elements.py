#User function Template for python3
#import os
#os.system("pip install sortedcontainers")
class Solution:
    #Function to return k largest elements from an array.
    def kLargest(self,li,n,k):
        li.sort(reverse=True)
        return li[:k]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t=int(input())
for _ in range(t):
    li = [int(x) for x in input().strip().split()]
    n=li[0]
    k=li[1]
    li = [int(x) for x in input().strip().split()]
    ob=Solution()
    k_largest_list = ob.kLargest(li,n,k)
    
    for element in k_largest_list:
        print(element, end = ' ')
    print('')
# } Driver Code Ends