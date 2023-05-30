class Solution:
    def second(n,arr):
        m = max(arr)
        mx = arr[0]
        for i in range(n):
            pick = arr[i]
            if pick!=m:
                mx = max(mx,pick)
        return mx