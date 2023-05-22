class Solution:
    def maxSubArraySum(self,arr,N):
        Max_Sum= arr[0]
        curr = arr[0]
        for i in range(1,N):
            if (curr + arr[i])>arr[i] :
                curr += arr[i]
            else:
                curr = arr[i]
            if curr>Max_Sum :
                Max_Sum = curr
        return Max_Sum
                
                

            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends