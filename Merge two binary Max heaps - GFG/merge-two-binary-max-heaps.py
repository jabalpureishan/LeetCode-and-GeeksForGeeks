#User function Template for python3
from heapq import heapify,heappush
class Solution():
    def mergeHeaps(self, a, b, n, m):
        heap = []
        heapify([])
        for i in a:
            heappush(heap,-i)
        for i in b:
            heappush(heap,-i)
        new = heap[:]
        for i in range(len(heap)):
            new[i] = -new[i]
        return new


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def isMerged(arr1, arr2, merged):
    if (len(arr1) + len(arr2) != len(merged)):
        return False
    arr1 += arr2
    arr1.sort()
    mergedCopy = sorted(merged)
    if (arr1 != mergedCopy):
        return False
    for i in range(1, len(merged)):
        if merged[i] > merged[(i-1)//2]:
            return False

    return True

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        a = [int(i) for i in input().split()]
        b = [int(i) for i in input().split()]
        copyA = a[:]
        copyB = b[:]
        obj = Solution()
        merged = obj.mergeHeaps(a, b, n, m)
        flag = isMerged(copyA, copyB, merged)
        print(0 if flag == False else 1)

# } Driver Code Ends