class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        arr = Counter(arr)
        dis = []
        for i in arr:
            if arr[i]==1:
                k -= 1 
                if k==0:
                    return i
        return ""
        