class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n,curr,count = len(arr),arr[0],0
        arr.append(-1)
        for i in arr:
            if i==curr:
                count += 1
                if count>n/4:
                    return i
            else:
                curr = i
                count = 1