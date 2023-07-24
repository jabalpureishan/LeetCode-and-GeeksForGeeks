from typing import List


class Solution:
    def kthLargest(self, N : int, K : int, Arr : List[int]) -> int:
        out = []
        for i in range(1,N+1):
            window = i
            slides = N - window
            Sum = sum(Arr[:window])
            out.append(Sum)
            for j in range(slides):
                Sum += Arr[window]
                Sum -= Arr[j]
                window += 1
                out.append(Sum)
        out.sort(reverse=True)
        return out[K-1]
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        K = int(input())
        
        
        Arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.kthLargest(N, K, Arr)
        
        print(res)
        

# } Driver Code Ends