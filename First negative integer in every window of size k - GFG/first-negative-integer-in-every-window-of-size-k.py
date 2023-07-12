#User function Template for python3
from collections import deque
def printFirstNegativeInteger( A, N, K):
        q = deque([])
        out = []
        for i in range(K):
            if A[i]<0:
                q.append(A[i])
        if len(q)>0:
            out.append(q[0])
        else:
            out.append(0)
        slides = len(A) - K
        for j in range(slides):
            if A[j]<0:
                q.popleft()
            if A[K]<0:
                q.append(A[K])
            K+=1
            if len(q)>0:
                out.append(q[0])
            else:
                out.append(0)
        return out


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends