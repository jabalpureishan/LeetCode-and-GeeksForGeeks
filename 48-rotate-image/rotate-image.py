class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r,c = len(matrix),len(matrix[0])
        for i in range(c):
            for j in range(i):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(r):
            matrix[i] = matrix[i][::-1]