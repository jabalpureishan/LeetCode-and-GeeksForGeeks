class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        arr = Counter(arr)
        arr = sorted(arr.items(),key=lambda x:x[1])
        n,ind = len(arr),0
        while ind<len(arr) and k>0:
            if k<arr[ind][1]:
                break
            else:
                k -= arr[ind][1]
                n -= 1
            ind += 1
        return n