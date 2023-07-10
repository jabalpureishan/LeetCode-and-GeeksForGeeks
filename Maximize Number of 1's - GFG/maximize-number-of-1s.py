#User function Template for python3


# m is maximum of number zeroes allowed 
# to flip, n is size of array 
def findZeroes(arr, n, m) :
        k=m
        nums = arr
        Max = j = 0
        d = {1:0,0:0}
        for i in range(len(nums)):
            d[nums[i]] += 1
            while(d[0]>k):
                d[nums[j]] -= 1
                j += 1
            Max = max(Max,d[0]+d[1])
        return Max


#{ 
 # Driver Code Starts
#Initial Template for Python 3




# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int , input().strip().split()))
        m=int(input())
        ans= findZeroes(arr, n, m)
        print(ans)
        tc=tc-1
# } Driver Code Ends