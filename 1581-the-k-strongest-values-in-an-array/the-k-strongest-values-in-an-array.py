class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()
        n = len(arr)
        
        med = arr[(n-1)//2]
        print(med)
        arr.sort(key=lambda x:abs(x-med))
        return arr[-k:]
        