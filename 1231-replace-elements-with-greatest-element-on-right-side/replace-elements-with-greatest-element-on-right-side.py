class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n,Max = len(arr),-1
        for i in range(n-1,-1,-1):
            temp = Max
            Max = max(Max,arr[i])
            arr[i] = temp
            
        return arr
        