#User function Template for python3

class Solution:
    def maxSumPairWithDifferenceLessThanK(self, arr, N, K): 
        arr.sort(reverse=True)
        #print("arr:",arr)
        ind = 0
        Sum = 0
        while(ind<N-1):
            if arr[ind]-arr[ind+1]<K:
                #print("1:",arr[ind],"2:",arr[ind+1])
                Sum += arr[ind] + arr[ind+1]
                ind += 2
            else:
                ind += 1
        return Sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        arr = [int(x) for x in input().strip().split()]
        K = int(input())
        ob=Solution()
        print( ob.maxSumPairWithDifferenceLessThanK(arr, N, K) )

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends