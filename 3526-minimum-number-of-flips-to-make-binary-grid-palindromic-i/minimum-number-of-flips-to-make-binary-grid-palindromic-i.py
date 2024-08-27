class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        n,m,row,col = len(grid),len(grid[0]),0,0
        for i in range(n//2):
            for j in range(m):
                if grid[i][j]!=grid[-(i+1)][j]: row += 1
        for i in range(n):
            for j in range(m//2):
                if grid[i][j]!=grid[i][-(j+1)]: col += 1
        return min(row,col)