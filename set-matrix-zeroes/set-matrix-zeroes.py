class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,column = set(),set()
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                if matrix[i][j]==0:
                    row.add(i)
                    column.add(j)
        #print("make:",make)
        for i in range(rows):
            for j in range(columns):
                if((i in row) or (j in column)):
                    matrix[i][j]=0
        return matrix