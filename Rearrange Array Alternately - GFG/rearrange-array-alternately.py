#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n):
        if n==1 :
            return arr
        Output = arr[:]
        arr.clear()
        flag = True
        if n%2==0 :
            l = n//2
        else:
            flag =False
            l = (n+1)//2
        for i in range(l):
            arr.append(Output[-(i+1)])
            arr.append(Output[i])
        if flag==False:
            arr.pop(-1)


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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends