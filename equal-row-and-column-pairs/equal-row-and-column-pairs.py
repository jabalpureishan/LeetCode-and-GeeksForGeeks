class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        Rows = []
        length = len(grid)
        for i in range(length):
            row = []
            for j in range(length):
                row.append(grid[j][i])
            Rows.append(tuple(row))
        D = {}
        for i in Rows:
            D[i] = D.get(i,0) + 1
        count = 0
        for i in grid:
            i = tuple(i)
            count += D.get(i,0)
        return count

        return 1