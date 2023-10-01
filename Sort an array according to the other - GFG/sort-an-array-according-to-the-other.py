#User function Template for python3

class Solution:
    # A1[] : the input array-1
    # N : size of the array A1[]
    # A2[] : the input array-2
    # M : size of the array A2[]
    
    #Function to sort an array according to the other array.
    def relativeSort (self,A1, N, A2, M):
        length = len(A2)
        ind = {}
        for i in range(length):
            if A2[i] not in ind:
                ind[A2[i]] = i
        notin = []
        inn = []
        for i in A1:
            if i in ind:
                inn.append(i)
            else:
                notin.append(i)
        #print(inn,notin)
        inn.sort(key=lambda x:ind[x])
        notin.sort()
        #print(inn,notin)
        return inn+notin


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int (input ())
    while t > 0:
        n, m = list(map(int, input().split()))
        a1 = list(map(int, input().split()))
        a2 = list(map(int, input().split()))
        
        ob=Solution()
        a1 = ob.relativeSort (a1, n, a2, m)
        print (*a1, end = " ")
        
        print ()
        
        t -= 1

# } Driver Code Ends