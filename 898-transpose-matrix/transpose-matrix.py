class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        output = []
        for i in range(columns):
            output.append([])
            for j in range(rows):
                output[i].append(matrix[j][i])
        return output