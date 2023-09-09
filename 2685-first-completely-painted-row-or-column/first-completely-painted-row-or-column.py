class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        indices = {}
        for i in range(len(arr)):
            if arr[i] not in indices:
                indices[arr[i]] = i
        rows =  len(mat)
        col = len(mat[0])
        Min = rows*col
        for i in mat:
            Max = 0
            for j in i:
                Max = max(indices[j],Max)
            Min = min(Min,Max)
        for i in range(col):
            Max = 0
            for j in mat:
                Max = max(indices[j[i]],Max)
            Min = min(Min,Max)
        return Min
        