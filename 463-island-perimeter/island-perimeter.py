class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        total = 0
        for i in range(rows):
            for j in range(columns):
                if grid[i][j]==1:
                    if j!=0:
                        if grid[i][j-1]==0:
                            total += 1
                    else:
                        total += 1
                    if i!=rows-1:
                        if grid[i+1][j]==0:
                            total += 1
                    else:
                        total += 1
                    if i!=0:
                        if grid[i-1][j]==0:
                            total += 1
                    else:
                        total += 1
                    if j!=columns-1:
                        if grid[i][j+1]==0:
                            total += 1
                    else:
                        total += 1
        return total