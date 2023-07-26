#User function Template for python3

def longestSubarry( A, N):
        A.append(-1)
        Max = count = 0
        for i in range(N+1):
            if A[i]>=0:
                count += 1
            else:
                Max = max(Max,count)
                count = 0
        return Max
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(longestSubarry(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends