from typing import List


class Solution:
    def smallerSum(self, n : int, arr : List[int]) -> List[int]:
        new = arr[:]
        new.sort()
        D = {}
        Sum = 0
        for i in new:
            if i not in D:
                D[i] = Sum
            Sum += i
        out = []
        for i in arr:
            out.append(D.get(i))
        return out
        



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
        
        n = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.smallerSum(n, arr)
        
        IntArray().Print(res)
        

# } Driver Code Ends