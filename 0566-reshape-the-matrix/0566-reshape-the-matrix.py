class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if (r*c)!=(len(mat)*len(mat[0])):
            return mat
        array = []
        for i in mat:
            array.extend(i)
        out = []
        Index = 0
        for i in range(r):
            out.append([])
            for j in range(c):
                out[i].append(array[Index])
                Index += 1
        return out
