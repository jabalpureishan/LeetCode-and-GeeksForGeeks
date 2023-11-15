class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        curr = 1
        Max = float("-inf")
        for i in range(len(arr)):
            if arr[i]>=curr:
                arr[i] = curr
                curr += 1
            Max = max(Max,arr[i])
        return Max
        