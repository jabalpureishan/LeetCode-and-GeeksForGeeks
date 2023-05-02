
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        window = K
        slides =  N - K + 1
        first = A[0:K]
        Output = [len(set(first))]
        d = {}
        for i in first:
            d[i] = d.get(i,0) + 1
        for i in range(1,slides):
            Add = A[window]
            Remove = A[i-1]
            d[Add] = d.get(Add,0) + 1
            d[Remove] = d.get(Remove) - 1
            if d.get(Remove)==0 :
                d.pop(Remove)
            Output.append(len(d))
            window+=1
        return Output


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends