from sortedcontainers import SortedList
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        length = len(arr)
        l = SortedList([])
        r = SortedList(arr[1:])
        for i in range(length):
            if i==0:
                if arr[i]>(r[-1]):
                    return 0
                l.add(arr[i])
                r.remove(arr[i+1])
            elif i==length-1:
                if arr[length-1]>(l[-1]):
                    return i
            else:
                if arr[i]>(r[-1]) and arr[i]>(l[-1]) :
                    return i
                l.add(arr[i])
                r.remove(arr[i+1])