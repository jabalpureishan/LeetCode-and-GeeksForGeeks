# Your task is to ocomplete this function
# Function should return an integer
def findEquilibrium(a,n):
        A,N = a,n
        after = sum(A)
        before =0
        for i in range(N):
            curr = A[i]
            after -= curr
            if after==before:
                return i
            before += curr
        return -1



#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(findEquilibrium(arr,n))
# Contributed By: Harshit Sidhwa

# } Driver Code Ends